# app.py — Flask server for the Document Humanizer
# Run with: python3.13 app.py  (or use start.bat)

import os
import sys
import uuid
import json
import time
import traceback
import threading

# Configure PyTorch CPU threads BEFORE any other torch operations.
# Must happen before transformers/model imports or set_num_interop_threads silently fails.
try:
    import torch
    torch.set_num_threads(2)
    torch.set_num_interop_threads(2)
except Exception:
    pass
from flask import Flask, request, jsonify, send_file, render_template, Response

IS_VERCEL = os.environ.get('VERCEL') == '1'
HF_SPACE_URL = os.environ.get('HF_SPACE_URL')
HF_API_TOKEN = (
    os.environ.get('HF_API_TOKEN') or 
    os.environ.get('HF_TOKEN') or 
    os.environ.get('humanizeread') or 
    os.environ.get('zeal000') or 
    os.environ.get('HF_READ_TOKEN')
)


# Try importing ML dependencies. If they are missing, we MUST run in proxy mode.
try:
    from humanizer.pipeline import humanize_docx, preload_model
    from humanizer.detector import score_docx
    import nltk
    HAS_LOCAL_DEPS = True
except (ImportError, ModuleNotFoundError):
    HAS_LOCAL_DEPS = False

# We force Proxy Mode if explicitly requested or if local ML dependencies are missing
USE_PROXY = IS_VERCEL or (HF_SPACE_URL is not None) or not HAS_LOCAL_DEPS

if USE_PROXY:
    print(f"[Proxy Mode] Routing requests to private Hugging Face Space: {HF_SPACE_URL}")
    import requests
else:
    # Force all AI models and dictionaries to download locally into the project folder
    # so the project is 100% portable
    MODELS_DIR = os.path.join(os.path.dirname(__file__), 'models')

    if not os.environ.get('HF_HOME'):
        os.environ['HF_HOME'] = os.path.join(MODELS_DIR, 'huggingface')
        os.makedirs(os.environ['HF_HOME'], exist_ok=True)

    if not os.environ.get('NLTK_DATA'):
        os.environ['NLTK_DATA'] = os.path.join(MODELS_DIR, 'nltk_data')
        os.makedirs(os.environ['NLTK_DATA'], exist_ok=True)

    def init_nltk():
        import os
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
        """Pre-load the AI models in a background thread so first requests are instant."""
        if __name__ == '__main__':
            if os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
                print("[Model] Reloader watchdog process detected. Skipping model preload.")
                return

        def _preload_all():
            try:
                preload_model()
            except Exception as e:
                print(f"[Model] Preloading humanizer model failed: {e}")
            try:
                from humanizer.detector import load_detector
                load_detector()
            except Exception as e:
                print(f"[Model] Preloading detector model failed: {e}")

        t = threading.Thread(target=_preload_all, daemon=True)
        t.start()

    init_nltk()
    init_model()

app = Flask(__name__)

# Helper to forward requests to the Hugging Face Space
def forward_request(path, method='GET', json_data=None, files=None, params=None, stream=False):
    if not HF_SPACE_URL:
        raise ValueError("HF_SPACE_URL environment variable is not configured in Vercel settings. Please set it in your Vercel Dashboard -> Settings -> Environment Variables.")
    url = f"{HF_SPACE_URL.rstrip('/')}/{path}"
    headers = {}
    if HF_API_TOKEN:
        headers['Authorization'] = f"Bearer {HF_API_TOKEN}"
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            json=json_data,
            files=files,
            params=params,
            stream=stream,
            timeout=180
        )
        return response
    except Exception as e:
        print(f"Proxy error to {url}: {e}")
        raise e

# Temp folder for uploads and outputs
if IS_VERCEL:
    # /tmp is the only writable directory on Vercel's Serverless environment
    UPLOAD_FOLDER = '/tmp'
else:
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'temp')
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {'docx'}


def allowed_file(filename: str) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return jsonify({
            'error': 'Failed to render index.html',
            'exception': str(e),
            'traceback': traceback.format_exc(),
            'cwd': os.getcwd(),
            'dir_contents': os.listdir('.') if os.path.exists('.') else []
        }), 500


@app.route('/scan', methods=['POST'])
def scan():
    """Score a .docx file for AI likelihood without modifying it."""
    if USE_PROXY:
        files = {k: (v.filename, v.read(), v.mimetype) for k, v in request.files.items()}
        try:
            res = forward_request('scan', 'POST', files=files)
            return (res.content, res.status_code, [('Content-Type', res.headers.get('Content-Type', 'application/json'))])
        except Exception as e:
            return jsonify({'error': f'Proxy error: {str(e)}'}), 500

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
    if USE_PROXY:
        def generate():
            try:
                url = f"{HF_SPACE_URL.rstrip('/')}/stream/{task_id}"
                headers = {}
                if HF_API_TOKEN:
                    headers['Authorization'] = f"Bearer {HF_API_TOKEN}"
                res = requests.request(
                    method='GET',
                    url=url,
                    headers=headers,
                    stream=True,
                    timeout=300
                )
                for line in res.iter_lines():
                    yield line + b'\n'
            except Exception as e:
                yield f"data: {json.dumps({'status': 'error', 'error': f'Proxy stream error: {str(e)}'})}\n\n".encode('utf-8')
        return Response(generate(), mimetype="text/event-stream")

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
    if USE_PROXY:
        files = {k: (v.filename, v.read(), v.mimetype) for k, v in request.files.items()}
        try:
            res = forward_request('start_task_doc', 'POST', files=files)
            return (res.content, res.status_code, [('Content-Type', res.headers.get('Content-Type', 'application/json'))])
        except Exception as e:
            return jsonify({'error': f'Proxy error: {str(e)}'}), 500

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
    if USE_PROXY:
        try:
            res = forward_request(f'download_doc/{task_id}', 'GET')
            headers = [
                ('Content-Type', res.headers.get('Content-Type', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document')),
                ('Content-Disposition', res.headers.get('Content-Disposition', f'attachment; filename=humanized_{task_id}.docx'))
            ]
            if 'X-Stats' in res.headers:
                headers.append(('X-Stats', res.headers['X-Stats']))
            if 'Access-Control-Expose-Headers' in res.headers:
                headers.append(('Access-Control-Expose-Headers', res.headers['Access-Control-Expose-Headers']))
            return (res.content, res.status_code, headers)
        except Exception as e:
            return jsonify({'error': f'Proxy error: {str(e)}'}), 500

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
    if USE_PROXY:
        try:
            res = forward_request('scan_text', 'POST', json_data=request.get_json())
            return (res.content, res.status_code, [('Content-Type', res.headers.get('Content-Type', 'application/json'))])
        except Exception as e:
            return jsonify({'error': f'Proxy error: {str(e)}'}), 500

    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided.'}), 400
    
    from humanizer.detector import score_text
    
    try:
        text = data['text']
        result = score_text(text, return_chunks=True)
        return jsonify(result)
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500


@app.route('/start_task_text', methods=['POST'])
def start_task_text():
    """Humanize raw text directly asynchronously."""
    if USE_PROXY:
        try:
            res = forward_request('start_task_text', 'POST', json_data=request.get_json())
            return (res.content, res.status_code, [('Content-Type', res.headers.get('Content-Type', 'application/json'))])
        except Exception as e:
            return jsonify({'error': f'Proxy error: {str(e)}'}), 500

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
    if USE_PROXY:
        try:
            res = forward_request(f'download_text/{task_id}', 'GET')
            return (res.content, res.status_code, [('Content-Type', res.headers.get('Content-Type', 'application/json'))])
        except Exception as e:
            return jsonify({'error': f'Proxy error: {str(e)}'}), 500

    if task_id not in ACTIVE_TASKS or ACTIVE_TASKS[task_id]["status"] != "done":
        return jsonify({"error": "Not found or not finished"}), 404
    task = ACTIVE_TASKS.pop(task_id, None)
    if task is None:
        return jsonify({"error": "Already cleaned up"}), 404
    return jsonify(task["result"])

if __name__ == '__main__':
    print("\n>>> Humanizer running at http://localhost:5000\n")
    app.run(debug=True, port=5000)
