// app.js — Drag-and-drop upload, processing animation, download handling

// ── STATE MANAGEMENT ──────────────────────────────────────────────────────────
const states = {
  upload:       document.getElementById('state-upload'),
  'text-input': document.getElementById('state-text-input'),
  processing:   document.getElementById('state-processing'),
  done:         document.getElementById('state-done'),
  error:        document.getElementById('state-error'),
};

function showState(name) {
  Object.entries(states).forEach(([key, el]) => {
    el.classList.toggle('active', key === name);
  });
}

// ── ELEMENTS ──────────────────────────────────────────────────────────────────
const dropZone       = document.getElementById('drop-zone');
const fileInput      = document.getElementById('file-input');
const filePreview    = document.getElementById('file-preview');
const fileNameEl     = document.getElementById('file-name-display');
const fileSizeEl     = document.getElementById('file-size-display');
const removeFileBtn  = document.getElementById('remove-file');
const submitBtn      = document.getElementById('submit-btn');
const downloadBtn    = document.getElementById('download-btn');
const restartBtn     = document.getElementById('restart-btn');
const retryBtn       = document.getElementById('retry-btn');
const errorMsgEl     = document.getElementById('error-msg');
const passItems      = document.querySelectorAll('.pass-item');

// Results
const resParagraphs  = document.getElementById('res-paragraphs');
const resTotal       = document.getElementById('res-total');
const resPhrases     = document.getElementById('res-phrases');
const breakdownGrid  = document.getElementById('breakdown-grid');

let selectedFile = null;
let downloadUrl  = null;

// Mode
let currentMode = 'doc'; // 'doc' or 'text'
const modeDocBtn     = document.getElementById('mode-doc');
const modeTextBtn    = document.getElementById('mode-text');
const rawTextInput   = document.getElementById('raw-text-input');
const submitTextBtn  = document.getElementById('submit-text-btn');
const scanResultsText= document.getElementById('scan-results-text');
const scanPctText    = document.getElementById('scan-pct-text');
const scanLabelText  = document.getElementById('scan-label-text');
const rawTextOutCtn  = document.getElementById('raw-text-output-container');
const rawTextOutput  = document.getElementById('raw-text-output');
const copyTextBtn    = document.getElementById('copy-text-btn');

modeDocBtn.addEventListener('click', () => {
  currentMode = 'doc';
  modeDocBtn.classList.add('active');
  modeTextBtn.classList.remove('active');
  showState('upload');
});

modeTextBtn.addEventListener('click', () => {
  currentMode = 'text';
  modeTextBtn.classList.add('active');
  modeDocBtn.classList.remove('active');
  showState('text-input');
});

// ── FILE FORMATTING ───────────────────────────────────────────────────────────
function formatBytes(bytes) {
  if (bytes < 1024) return bytes + ' B';
  if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + ' KB';
  return (bytes / (1024 * 1024)).toFixed(2) + ' MB';
}

// ── FILE SELECTION ────────────────────────────────────────────────────────────
function selectFile(file) {
  if (!file) return;
  if (!file.name.endsWith('.docx')) {
    showError('Only .docx files are supported. Please upload a Word document.');
    return;
  }
  selectedFile = file;
  fileNameEl.textContent = file.name;
  fileSizeEl.textContent = formatBytes(file.size);
  filePreview.classList.remove('hidden');
  submitBtn.disabled = false; // Enabled immediately so the user can process without waiting for scan
  scanFile(file);
}

async function scanFile(file) {
  const formData = new FormData();
  formData.append('file', file);
  
  const scanResults = document.getElementById('scan-results');
  const scanPct = document.getElementById('scan-pct');
  const scanLabel = document.getElementById('scan-label');
  
  scanResults.classList.remove('hidden');
  scanPct.textContent = '--%';
  scanLabel.textContent = 'Scanning...';
  
  const viewerBtn = document.getElementById('toggle-viewer-btn');
  const viewer = document.getElementById('document-viewer');
  viewerBtn.classList.add('hidden');
  viewer.classList.add('hidden');
  viewer.innerHTML = '';
  
  try {
    const res = await fetch('/scan', { method: 'POST', body: formData });
    const data = await res.json();
    if (data.overall_pct !== undefined) {
      const pct = data.overall_pct;
      scanPct.textContent = pct + '%';
      if (pct > 50) {
        scanLabel.textContent = 'High AI Likelihood';
        scanPct.style.color = 'var(--orange)';
      } else {
        scanLabel.textContent = 'Likely Human';
        scanPct.style.color = 'var(--green)';
      }
      
      // Render chunks
      if (data.chunks && data.chunks.length > 0) {
        const legend = document.createElement('div');
        legend.innerHTML = `
          <div style="margin-bottom: 16px; padding-bottom: 12px; border-bottom: 1px solid var(--border); font-weight: bold; font-size: 12px; display: flex; gap: 12px; justify-content: center;">
            <span style="background: rgba(255, 50, 50, 0.15); padding: 4px 8px; border-radius: 4px;">🔴 High AI (≥ 50%)</span>
            <span style="background: rgba(255, 200, 50, 0.15); padding: 4px 8px; border-radius: 4px;">🟡 Medium AI (30-49%)</span>
          </div>
        `;
        viewer.appendChild(legend);
        
        data.chunks.forEach(chunk => {
          const p = document.createElement('p');
          p.textContent = chunk.text;
          p.style.marginBottom = '12px';
          p.style.padding = '4px 8px';
          p.style.borderRadius = '4px';
          
          if (chunk.pct >= 50) {
            p.style.background = 'rgba(255, 50, 50, 0.15)'; // Red for AI
          } else if (chunk.pct >= 30) {
            p.style.background = 'rgba(255, 200, 50, 0.15)'; // Yellow for Medium
          }
          viewer.appendChild(p);
        });
        viewerBtn.classList.remove('hidden');
      }
      
      submitBtn.disabled = false;
    } else {
      scanLabel.textContent = 'Scan failed';
      submitBtn.disabled = false;
    }
  } catch (err) {
    scanLabel.textContent = 'Scan failed';
    submitBtn.disabled = false;
  }
}

// Viewer toggle
document.getElementById('toggle-viewer-btn').addEventListener('click', function() {
  const viewer = document.getElementById('document-viewer');
  if (viewer.classList.contains('hidden')) {
    viewer.classList.remove('hidden');
    this.textContent = 'Hide AI Highlights';
  } else {
    viewer.classList.add('hidden');
    this.textContent = 'View AI Highlights';
  }
});

function clearFile() {
  selectedFile = null;
  fileInput.value = '';
  filePreview.classList.add('hidden');
  submitBtn.disabled = true;
  // Also hide and reset scan results
  const scanResults = document.getElementById('scan-results');
  const scanPct = document.getElementById('scan-pct');
  const scanLabel = document.getElementById('scan-label');
  const viewerBtn = document.getElementById('toggle-viewer-btn');
  const viewer = document.getElementById('document-viewer');
  scanResults.classList.add('hidden');
  scanPct.textContent = '--%';
  scanLabel.textContent = 'Scanning...';
  viewerBtn.classList.add('hidden');
  viewer.classList.add('hidden');
  viewer.innerHTML = '';
}

// ── DRAG AND DROP ─────────────────────────────────────────────────────────────
dropZone.addEventListener('dragover', (e) => {
  e.preventDefault();
  dropZone.classList.add('dragover');
});
dropZone.addEventListener('dragleave', () => dropZone.classList.remove('dragover'));
dropZone.addEventListener('drop', (e) => {
  e.preventDefault();
  dropZone.classList.remove('dragover');
  const file = e.dataTransfer?.files?.[0];
  if (file) selectFile(file);
});
dropZone.addEventListener('keydown', (e) => {
  if (e.key === 'Enter' || e.key === ' ') fileInput.click();
});

fileInput.addEventListener('change', () => {
  if (fileInput.files.length) selectFile(fileInput.files[0]);
});

removeFileBtn.addEventListener('click', (e) => {
  e.stopPropagation();
  clearFile();
});

function resetPasses() {
  document.getElementById('progress-pct-label').textContent = '0%';
  document.getElementById('progress-bar-fill').style.width = '0%';
  document.getElementById('progress-status-msg').textContent = 'Initializing...';
}

// ── SUBMIT DOC ────────────────────────────────────────────────────────────────
submitBtn.addEventListener('click', uploadAndProcess);

async function uploadAndProcess() {
  if (!selectedFile) return;

  showState('processing');
  resetPasses();

  const formData = new FormData();
  formData.append('file', selectedFile);

  try {
    const res = await fetch('/start_task_doc', { method: 'POST', body: formData });
    if (!res.ok) {
        let errMsg = 'Processing failed. Please try again.';
        try { const data = await res.json(); errMsg = data.error || errMsg; } catch (_) {}
        showError(errMsg);
        return;
    }
    
    const data = await res.json();
    const taskId = data.task_id;
    
    const source = new EventSource('/stream/' + taskId);
    
    source.onmessage = async (e) => {
      const task = JSON.parse(e.data);
      
      document.getElementById('progress-pct-label').textContent = task.progress + '%';
      document.getElementById('progress-bar-fill').style.width = task.progress + '%';
      document.getElementById('progress-status-msg').textContent = task.message;
      
      if (task.status === 'done') {
        source.close();
        const stats = task.result.stats;
        
        downloadBtn.href = '/download_doc/' + taskId;
        downloadBtn.download = task.result.download_name;

        showResults(stats);
        showState('done');
        
        document.getElementById('final-scan-old').textContent = Math.round(stats.before * 100) + '%';
        document.getElementById('final-scan-new').textContent = Math.round(stats.after * 100) + '%';

        animateNumber(resParagraphs, stats.paragraphs);
        animateNumber(resTotal,      stats.total);
        animateNumber(resPhrases,    stats.pass1);

        renderBreakdown(stats);
      } else if (task.status === 'error') {
        source.close();
        showError(task.error || 'Task failed');
      }
    };
    
    source.onerror = () => {
      source.close();
      showError('Connection to server lost.');
    };

  } catch (err) {
    console.error(err);
    showError('Connection error. Make sure the server is running.');
  }
}

// ── TEXT HANDLING ─────────────────────────────────────────────────────────────
let textScanTimeout = null;
let latestTextScore = 0;

rawTextInput.addEventListener('input', () => {
  const text = rawTextInput.value.trim();
  const words = text.split(/\s+/).filter(w=>w).length;
  if (text.length === 0 || words < 20) {
    submitTextBtn.disabled = true;
    scanResultsText.classList.add('hidden');
    return;
  }
  
  submitTextBtn.disabled = false;
  scanResultsText.classList.remove('hidden');
  scanPctText.textContent = '--%';
  scanLabelText.textContent = 'Scanning...';
  
  clearTimeout(textScanTimeout);
  textScanTimeout = setTimeout(async () => {
    try {
      const res = await fetch('/scan_text', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text })
      });
      const data = await res.json();
      if (data.overall_pct !== undefined) {
        latestTextScore = data.overall_pct;
        scanPctText.textContent = data.overall_pct + '%';
        if (data.overall_pct > 50) {
          scanLabelText.textContent = 'High AI Likelihood';
          scanPctText.style.color = 'var(--orange)';
        } else {
          scanLabelText.textContent = 'Likely Human';
          scanPctText.style.color = 'var(--green)';
        }
      }
    } catch (err) {
      scanLabelText.textContent = 'Scan failed';
    }
  }, 800);
});

submitTextBtn.addEventListener('click', async () => {
  const text = rawTextInput.value.trim();
  if (!text) return;

  showState('processing');
  resetPasses();
  
  try {
    const res = await fetch('/start_task_text', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text })
    });
    
    if (!res.ok) {
      let errMsg = 'Processing failed.';
      try { const d = await res.json(); errMsg = d.error || errMsg; } catch (_) {}
      showError(errMsg);
      return;
    }
    
    const d = await res.json();
    const taskId = d.task_id;
    const source = new EventSource('/stream/' + taskId);
    
    source.onmessage = async (e) => {
      const task = JSON.parse(e.data);
      document.getElementById('progress-pct-label').textContent = task.progress + '%';
      document.getElementById('progress-bar-fill').style.width = task.progress + '%';
      document.getElementById('progress-status-msg').textContent = task.message;
      
      if (task.status === 'done') {
        source.close();
        const data = task.result;
        rawTextOutput.value = data.text;
        
        downloadBtn.style.display = 'none';
        rawTextOutCtn.classList.remove('hidden');
        
        let afterScore = 0;
        try {
          const resAfter = await fetch('/scan_text', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text: data.text })
          });
          const dataAfter = await resAfter.json();
          if (dataAfter.overall_pct !== undefined) afterScore = dataAfter.overall_pct;
        } catch(e) {}
        
        showResults({});
        showState('done');
        
        document.getElementById('final-scan-old').textContent = Math.round(latestTextScore) + '%';
        document.getElementById('final-scan-new').textContent = Math.round(afterScore) + '%';

        animateNumber(resParagraphs, data.stats.paragraphs_processed);
        animateNumber(resTotal,      data.stats.total_changes);
        animateNumber(resPhrases,    data.stats.pass1_ai_phrases || 0);

        renderBreakdown({
            pass1: data.stats.pass1_ai_phrases || 0,
            pass2: data.stats.pass2_intensifiers || 0,
            pass3: data.stats.pass3_burstiness || 0,
            pass4: data.stats.pass4_discourse_markers || 0,
            pass5: data.stats.pass5_contractions || 0,
            pass6: data.stats.pass6_passive_voice || 0,
            pass7: data.stats.pass7_opener_diversity || 0
        });
        
        // Notify server we've downloaded it so it cleans up the task memory
        fetch('/download_text/' + taskId).catch(e => console.error(e));
        
      } else if (task.status === 'error') {
        source.close();
        showError(task.error || 'Failed');
      }
    };
    source.onerror = () => { source.close(); showError('Connection lost'); };
    
  } catch(err) {
    showError('Error humanizing text.');
  }
});

copyTextBtn.addEventListener('click', () => {
  rawTextOutput.select();
  document.execCommand('copy');
  const oldText = copyTextBtn.textContent;
  copyTextBtn.textContent = 'Copied!';
  setTimeout(() => copyTextBtn.textContent = oldText, 2000);
});

// ── COUNT-UP ANIMATION ────────────────────────────────────────────────────────
function animateNumber(el, target, duration = 800) {
  const start = performance.now();
  function tick(now) {
    const progress = Math.min((now - start) / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 3); // ease-out cubic
    el.textContent = Math.round(eased * target);
    if (progress < 1) requestAnimationFrame(tick);
  }
  requestAnimationFrame(tick);
}

// ── BREAKDOWN BARS ────────────────────────────────────────────────────────────
const PASS_LABELS = [
  'AI Phrases',
  'Intensifiers',
  'Burstiness',
  'Discourse Markers',
  'Contractions',
  'Passive Voice',
  'Opener Diversity',
];

function renderBreakdown(stats) {
  const counts = [
    stats.pass1, stats.pass2, stats.pass3, stats.pass4,
    stats.pass5, stats.pass6, stats.pass7,
  ];
  const maxVal = Math.max(...counts, 1);

  breakdownGrid.innerHTML = '';
  counts.forEach((count, i) => {
    const row = document.createElement('div');
    row.className = 'breakdown-row';
    row.innerHTML = `
      <span class="breakdown-label">${PASS_LABELS[i]}</span>
      <div class="breakdown-bar-wrap">
        <div class="breakdown-bar" id="bar-${i}"></div>
      </div>
      <span class="breakdown-count">${count}</span>
    `;
    breakdownGrid.appendChild(row);
  });

  // Animate bars after DOM insertion
  requestAnimationFrame(() => {
    counts.forEach((count, i) => {
      const bar = document.getElementById(`bar-${i}`);
      if (bar) {
        setTimeout(() => {
          bar.style.width = `${(count / maxVal) * 100}%`;
        }, i * 80);
      }
    });
  });
}

// ── RESULTS HELPER ────────────────────────────────────────────────────────────
function showResults(stats) {
  resParagraphs.textContent = '0';
  resTotal.textContent = '0';
  resPhrases.textContent = '0';
}

// ── ERROR ─────────────────────────────────────────────────────────────────────
function showError(msg) {
  errorMsgEl.textContent = msg;
  showState('error');
}

// ── RESTART ───────────────────────────────────────────────────────────────────
function restart() {
  clearFile();
  resetPasses();
  if (downloadUrl) {
    URL.revokeObjectURL(downloadUrl);
    downloadUrl = null;
  }
  document.getElementById('scan-results').classList.add('hidden');
  
  // reset text modes
  rawTextInput.value = '';
  rawTextOutput.value = '';
  scanResultsText.classList.add('hidden');
  submitTextBtn.disabled = true;
  rawTextOutCtn.classList.add('hidden');
  downloadBtn.style.display = ''; // restore
  
  if (currentMode === 'doc') {
    showState('upload');
  } else {
    showState('text-input');
  }
}

restartBtn.addEventListener('click', restart);
retryBtn.addEventListener('click', restart);
