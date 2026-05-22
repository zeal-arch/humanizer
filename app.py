# app.py — Flask server for the Document Humanizer
# Run with: python3.13 app.py  (or use start.bat)

import os
import sys

# Force all AI models and dictionaries to download locally into the project folder
# so the project is 100% portable
# On local dev: store everything inside the project's models/ folder (portable).
# On Hugging Face Spaces: use the default system cache dirs (set by HF infra).
MODELS_DIR = os.path.join(os.path.dirname(__file__), 'models')

if not os.environ.get('HF_HOME'):
    os.environ['HF_HOME'] = os.path.join(MODELS_DIR, 'huggingface')
    os.makedirs(os.environ['HF_HOME'], exist_ok=True)

if not os.environ.get('NLTK_DATA'):
    os.environ['NLTK_DATA'] = os.path.join(MODELS_DIR, 'nltk_data')
    os.makedirs(os.environ['NLTK_DATA'], exist_ok=True)


import uuid
import json
import time
import traceback
import threading
from flask import Flask, request, jsonify, send_file, render_template, Response
from humanizer.pipeline import humanize_docx, preload_model
from humanizer.detector import score_docx

import nltk

def init_nltk():
    import os
    # Download directly to the default NLTK data dir to ensure pipeline.py can find it
    corpora = [
        ('corpora/wordnet', 'wordnet'),
        ('corpora/omw-1.4', 'omw-1.4'),
        ('corpora/words', 'words'),
        ('tokenizers/punkt', 'punkt'),
        ('tokenizers/punkt_tab', 'punkt_tab'),
        ('taggers/averaged_perceptron_tagger', 'averaged_perceptron_tagger'),
        ('taggers/averaged_perceptron_tagger_eng', 'averaged_perceptron_tagger_eng'),
    ]
    for path, package in corpora:
        try:
            nltk.data.find(path)
        except LookupError:
            print(f"Downloading NLTK {package}...")
            nltk.download(package, download_dir=os.environ['NLTK_DATA'], quiet=True)

def init_model():
    """Pre-load the AI model in a background thread so first request is instant."""
    # Local dev server runs with debug=True, which spawns a parent watchdog and child worker.
    # We should only load the model in the child worker (where WERKZEUG_RUN_MAIN == 'true')
    # to avoid loading the model twice and thrashing GPU VRAM.
    # In production (e.g. Gunicorn/Docker), __name__ != '__main__', so we always preload.
    if __name__ == '__main__':
        if os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
            print("[Model] Reloader watchdog process detected. Skipping model preload.")
            return

    t = threading.Thread(target=preload_model, daemon=True)
    t.start()



init_nltk()
init_model()

app = Flask(__name__)

# Temp folder for uploads and outputs
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'temp')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {'docx'}


def allowed_file(filename: str) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/scan', methods=['POST'])
def scan():
    """Score a .docx file for AI likelihood without modifying it."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided.'}), 400

    file = request.files['file']
    if not allowed_file(file.filename):
        return jsonify({'error': 'Only .docx files are supported.'}), 400

    uid = uuid.uuid4().hex
    input_path = os.path.join(UPLOAD_FOLDER, f'scan_{uid}.docx')
    try:
        file.save(input_path)
        result = score_docx(input_path)
        return jsonify(result)
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500
    finally:
        if os.path.exists(input_path):
            try:
                os.remove(input_path)
            except Exception:
                pass

ACTIVE_TASKS = {}


@app.route('/stream/<task_id>')
def stream(task_id):
    def generate():
        last_progress = -1
        last_msg = ""
        while True:
            if task_id not in ACTIVE_TASKS:
                yield f"data: {json.dumps({'status': 'error', 'error': 'Task not found'})}\n\n"
                break
            
            task = ACTIVE_TASKS[task_id]
            
            # Only yield if changed to save bandwidth, or every 1s
            yield f"data: {json.dumps(task)}\n\n"
            
            if task["status"] in ["done", "error"]:
                break
            time.sleep(0.5)
    return Response(generate(), mimetype="text/event-stream")


@app.route('/start_task_doc', methods=['POST'])
def start_task_doc():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided.'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected.'}), 400

    if not allowed_file(file.filename):
        return jsonify({'error': 'Only .docx files are supported.'}), 400

    task_id = uuid.uuid4().hex
    input_filename = f"input_{task_id}.docx"
    input_path = os.path.join(UPLOAD_FOLDER, input_filename)
    file.save(input_path)
    
    ACTIVE_TASKS[task_id] = {
        "status": "processing",
        "progress": 0,
        "message": "Initializing...",
        "result": None,
        "error": None
    }
    
    original_filename = file.filename

    def background_worker(t_id, in_path, orig_name):
        try:
            ACTIVE_TASKS[t_id]["message"] = "Calculating initial AI score..."
            before_result = score_docx(in_path)
            before_score = before_result['overall_pct'] / 100.0

            output_filename = f"humanized_{t_id}.docx"
            out_path = os.path.join(UPLOAD_FOLDER, output_filename)
            
            def progress_cb(pct, _, msg):
                ACTIVE_TASKS[t_id]["progress"] = pct
                ACTIVE_TASKS[t_id]["message"] = msg
                
            stats = humanize_docx(in_path, out_path, progress_callback=progress_cb)

            ACTIVE_TASKS[t_id]["message"] = "Calculating final AI score..."
            after_result = score_docx(out_path)
            after_score = after_result['overall_pct'] / 100.0

            original_stem = os.path.splitext(orig_name)[0]
            download_name = f"{original_stem}_humanized.docx"

            try:
                os.remove(in_path)
            except Exception:
                pass
                
            p6 = sum([
                stats.get('pass6_passive_voice', 0), stats.get('pass7_opener_diversity', 0),
                stats.get('pass8_hedging', 0), stats.get('pass9_parentheticals', 0),
                stats.get('pass10_self_corrections', 0), stats.get('pass11_personal_voice', 0),
                stats.get('pass12_qualifiers', 0), stats.get('pass13_punctuation', 0)
            ])
            p7 = sum([
                stats.get('pass14_syntactic_fronting', 0),
                stats.get('pass15_synonym_rotation', 0),
                stats.get('pass16_imperfect_discourse', 0)
            ])

            ACTIVE_TASKS[t_id]["result"] = {
                "file_path": out_path,
                "download_name": download_name,
                "stats": {
                    "paragraphs": stats.get('paragraphs_processed', 0),
                    "total": stats.get('total_changes', 0),
                    "before": before_score,
                    "after": after_score,
                    "pass1": stats.get('pass1_ai_phrases', 0),
                    "pass2": stats.get('pass2_intensifiers', 0),
                    "pass3": stats.get('pass3_burstiness', 0),
                    "pass4": stats.get('pass4_discourse_markers', 0),
                    "pass5": stats.get('pass5_contractions', 0),
                    "pass6": p6,
                    "pass7": p7,
                }
            }
            ACTIVE_TASKS[t_id]["progress"] = 100
            ACTIVE_TASKS[t_id]["status"] = "done"

        except Exception as e:
            print(traceback.format_exc())
            ACTIVE_TASKS[t_id]["status"] = "error"
            ACTIVE_TASKS[t_id]["error"] = str(e)
            
    t = threading.Thread(target=background_worker, args=(task_id, input_path, original_filename))
    t.start()
    
    return jsonify({"task_id": task_id})


@app.route('/download_doc/<task_id>', methods=['GET'])
def download_doc(task_id):
    if task_id not in ACTIVE_TASKS or ACTIVE_TASKS[task_id]["status"] != "done":
        return "Not found or not finished", 404
        
    res = ACTIVE_TASKS[task_id]["result"]
    output_path = res["file_path"]
    
    response = send_file(
        output_path,
        as_attachment=True,
        download_name=res["download_name"],
        mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )
    
    # Send stats as headers too for easy frontend integration if needed,
    # though SSE provides them as well.
    response.headers['X-Stats'] = json.dumps(res["stats"])
    response.headers['Access-Control-Expose-Headers'] = 'X-Stats'
    
    @response.call_on_close
    def cleanup():
        try:
            if os.path.exists(output_path):
                os.remove(output_path)
            # Remove from active tasks
            if task_id in ACTIVE_TASKS:
                del ACTIVE_TASKS[task_id]
        except Exception:
            pass

    return response



@app.route('/scan_text', methods=['POST'])
def scan_text():
    """Score raw text for AI likelihood."""
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided.'}), 400
    
    from humanizer.detector import score_text
    
    try:
        text = data['text']
        # We need chunking logic to match docx
        paragraphs = [p.strip() for p in text.split('\n') if len(p.strip().split()) >= 5]
        if not paragraphs:
            # Fallback if too short
            paragraphs = [text.strip()] if text.strip() else []
            
        full_text = '\n'.join(paragraphs)
        word_count = len(full_text.split())
        result = score_text(full_text)
        
        chunks = []
        for block in paragraphs:
            block_score = score_text(block)
            chunks.append({
                'text': block,
                'pct': block_score['overall_pct']
            })
            
        result['word_count'] = word_count
        result['paragraph_count'] = len(paragraphs)
        result['chunks'] = chunks
        return jsonify(result)
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500


@app.route('/start_task_text', methods=['POST'])
def start_task_text():
    """Humanize raw text directly asynchronously."""
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided.'}), 400
        
    task_id = uuid.uuid4().hex
    original_text = data['text']
    
    ACTIVE_TASKS[task_id] = {
        "status": "processing",
        "progress": 0,
        "message": "Initializing...",
        "result": None,
        "error": None
    }
    
    def background_worker(t_id, text):
        try:
            from humanizer.pipeline import humanize_text
            
            all_stats = {
                'pass1_ai_phrases': 0, 'pass2_intensifiers': 0,
                'pass3_burstiness': 0, 'pass4_discourse_markers': 0,
                'pass5_contractions': 0, 'pass6_passive_voice': 0,
                'pass7_opener_diversity': 0, 'pass8_hedging': 0,
                'pass9_parentheticals': 0, 'pass10_self_corrections': 0,
                'pass11_personal_voice': 0, 'pass12_qualifiers': 0,
                'pass13_punctuation': 0, 'pass14_syntactic_fronting': 0,
                'pass15_synonym_rotation': 0, 'pass16_imperfect_discourse': 0,
                'pass17_ghost_characters': 0,
                'pass18_perplexity_tension': 0,
                'pass19_structural_smoothing': 0,
                'total_changes': 0,
                'paragraphs_processed': 0,
                'paragraphs_skipped': 0,
            }
            
            paragraphs = text.split('\n')
            out_paragraphs = []
            
            total_paras = len(paragraphs)
            
            for i, p in enumerate(paragraphs):
                ACTIVE_TASKS[t_id]["progress"] = int((i / max(total_paras, 1)) * 100)
                ACTIVE_TASKS[t_id]["message"] = f"Processing paragraph {i+1} of {total_paras}..."
                
                original_p = p.strip()
                if not original_p or len(original_p.split()) < 5:
                    out_paragraphs.append(p) 
                    all_stats['paragraphs_skipped'] += 1
                    continue
                    
                res = humanize_text(original_p)
                out_paragraphs.append(res['text'])
                
                if res['text'] != original_p:
                    for k, v in res['stats'].items():
                        if k in all_stats:
                            all_stats[k] += v
                    all_stats['paragraphs_processed'] += 1
                    
            all_stats['total_changes'] = sum(
                v for k, v in all_stats.items() if k.startswith('pass')
            )
            
            humanized = '\n'.join(out_paragraphs)
            
            ACTIVE_TASKS[t_id]["result"] = {
                "text": humanized,
                "stats": all_stats
            }
            ACTIVE_TASKS[t_id]["progress"] = 100
            ACTIVE_TASKS[t_id]["status"] = "done"
            
        except Exception as e:
            print(traceback.format_exc())
            ACTIVE_TASKS[t_id]["status"] = "error"
            ACTIVE_TASKS[t_id]["error"] = str(e)
            
    t = threading.Thread(target=background_worker, args=(task_id, original_text))
    t.start()
    
    return jsonify({"task_id": task_id})

@app.route('/download_text/<task_id>', methods=['GET'])
def download_text(task_id):
    if task_id not in ACTIVE_TASKS or ACTIVE_TASKS[task_id]["status"] != "done":
        return jsonify({"error": "Not found or not finished"}), 404
    res = ACTIVE_TASKS[task_id]["result"]
    del ACTIVE_TASKS[task_id]
    return jsonify(res)

if __name__ == '__main__':
    print("\n>>> Humanizer running at http://localhost:5000\n")
    app.run(debug=True, port=5000)
