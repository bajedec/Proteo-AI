/**
 * PROTEO AI - CAD & Sketch Studio
 * Client-Side Controller (Frontend)
 * Autor: Saul Adain Huillca Rodriguez (Desarrollador Frontend)
 */

document.addEventListener('DOMContentLoaded', () => {
  // Elements
  const dropzone = document.getElementById('dropzone');
  const fileInput = document.getElementById('fileInput');
  const fileNameLabel = document.getElementById('fileNameLabel');
  const fileSpecsLabel = document.getElementById('fileSpecsLabel');
  const previewInput = document.getElementById('previewInput');
  const previewOutput = document.getElementById('previewOutput');
  const runAiBtn = document.getElementById('runAiBtn');
  const runBtnText = document.getElementById('runBtnText');

  // Sliders & Controls
  const lineWeightInput = document.getElementById('lineWeightInput');
  const lineWeightVal = document.getElementById('lineWeightVal');
  const rdpInput = document.getElementById('rdpInput');
  const rdpVal = document.getElementById('rdpVal');
  const toggleBg = document.getElementById('toggleBg');
  const togglePin = document.getElementById('togglePin');
  const presetBtns = document.querySelectorAll('.style-preset-btn');
  const viewBtns = document.querySelectorAll('.view-mode-btn');
  const leftCanvasPanel = document.getElementById('leftCanvasPanel');

  // Telemetry HUD Elements
  const statLatency = document.getElementById('statLatency');
  const statPolylines = document.getElementById('statPolylines');
  const statStatus = document.getElementById('statStatus');

  // Download Buttons
  const downloadDxf = document.getElementById('downloadDxf');
  const downloadSvg = document.getElementById('downloadSvg');
  const downloadPng = document.getElementById('downloadPng');

  // State
  let currentFile = null;
  let activePreset = 'blueprint';
  let isBgIsolated = true;
  let downloadUrls = { dxf: null, svg: null, png: null };

  // 1. Sliders Event Listeners
  if (lineWeightInput) {
    lineWeightInput.addEventListener('input', (e) => {
      lineWeightVal.textContent = parseFloat(e.target.value).toFixed(2) + ' pt';
    });
  }

  if (rdpInput) {
    rdpInput.addEventListener('input', (e) => {
      rdpVal.textContent = 'ε = ' + parseFloat(e.target.value).toFixed(2);
    });
  }

  // 2. Preset Selection
  presetBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      presetBtns.forEach(b => {
        b.classList.remove('bg-surface-container-high', 'text-secondary', 'border-secondary/50');
        b.classList.add('bg-surface-container', 'text-on-surface-variant', 'border-transparent');
      });
      btn.classList.add('bg-surface-container-high', 'text-secondary', 'border-secondary/50');
      btn.classList.remove('bg-surface-container', 'text-on-surface-variant', 'border-transparent');
      activePreset = btn.getAttribute('data-preset');
    });
  });

  // 3. Toggle Subject Isolation
  if (toggleBg) {
    toggleBg.addEventListener('click', () => {
      isBgIsolated = !isBgIsolated;
      if (isBgIsolated) {
        toggleBg.classList.replace('bg-surface-container-highest', 'bg-secondary');
        togglePin.classList.replace('translate-x-0', 'translate-x-4');
      } else {
        toggleBg.classList.replace('bg-secondary', 'bg-surface-container-highest');
        togglePin.classList.replace('translate-x-4', 'translate-x-0');
      }
    });
  }

  // 4. Viewport Mode Switcher
  viewBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      viewBtns.forEach(b => {
        b.classList.remove('bg-surface-container-high', 'text-secondary', 'font-bold');
        b.classList.add('text-on-surface-variant');
      });
      btn.classList.add('bg-surface-container-high', 'text-secondary', 'font-bold');
      btn.classList.remove('text-on-surface-variant');

      const mode = btn.getAttribute('data-mode');
      if (mode === 'single') {
        leftCanvasPanel.classList.add('hidden');
      } else {
        leftCanvasPanel.classList.remove('hidden');
      }
    });
  });

  // 5. File Selection & Drag-and-Drop
  dropzone.addEventListener('click', () => fileInput.click());

  ['dragenter', 'dragover'].forEach(eventName => {
    dropzone.addEventListener(eventName, (e) => {
      e.preventDefault();
      dropzone.classList.add('border-secondary', 'bg-surface-container-high');
    });
  });

  ['dragleave', 'drop'].forEach(eventName => {
    dropzone.addEventListener(eventName, (e) => {
      e.preventDefault();
      dropzone.classList.remove('border-secondary', 'bg-surface-container-high');
    });
  });

  dropzone.addEventListener('drop', (e) => {
    const files = e.dataTransfer.files;
    if (files.length > 0) {
      handleFileSelected(files[0]);
    }
  });

  fileInput.addEventListener('change', (e) => {
    if (e.target.files.length > 0) {
      handleFileSelected(e.target.files[0]);
    }
  });

  function handleFileSelected(file) {
    const allowed = ['.png', '.jpg', '.jpeg'];
    const ext = '.' + file.name.split('.').pop().toLowerCase();
    if (!allowed.includes(ext)) {
      alert('Formato de archivo no válido. Solo se admiten archivos .PNG, .JPG o .JPEG.');
      return;
    }

    currentFile = file;
    fileNameLabel.textContent = file.name;
    const sizeMb = (file.size / (1024 * 1024)).toFixed(2);
    fileSpecsLabel.textContent = `${sizeMb} MB • Formato ${ext.toUpperCase()}`;

    // Read and preview input
    const reader = new FileReader();
    reader.onload = (event) => {
      previewInput.src = event.target.result;
    };
    reader.readAsDataURL(file);

    statStatus.textContent = 'FOTO CARGADA';
  }

  // 6. Run AI Processing Request
  runAiBtn.addEventListener('click', async () => {
    if (!currentFile) {
      alert('Por favor selecciona o arrastra una imagen antes de generar el boceto.');
      return;
    }

    // Set Loading State
    runAiBtn.disabled = true;
    runBtnText.textContent = 'PROCESANDO EN CPU...';
    statStatus.textContent = 'EXTRAYENDO TRAZOS...';

    const formData = new FormData();
    formData.append('file', currentFile);
    formData.append('preset', activePreset);
    formData.append('line_weight', lineWeightInput.value);
    formData.append('rdp_tolerance', rdpInput.value);
    formData.append('isolate_bg', isBgIsolated);

    try {
      const response = await fetch('/api/process', {
        method: 'POST',
        body: formData
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Error al procesar la imagen.');
      }

      const result = await response.json();

      // Update Result Preview
      previewOutput.src = result.sketch_url;

      // Update Telemetry HUD
      statLatency.textContent = `${result.latency}s LATENCIA`;
      statPolylines.textContent = `${result.polylines} POLILÍNEAS CAD`;
      statStatus.textContent = 'COMPLETADO';

      // Store Download URLs
      downloadUrls.dxf = result.dxf_url;
      downloadUrls.svg = result.svg_url;
      downloadUrls.png = result.png_url;

    } catch (err) {
      console.error(err);
      alert('Error: ' + err.message);
      statStatus.textContent = 'ERROR EN PROCESO';
    } finally {
      runAiBtn.disabled = false;
      runBtnText.textContent = 'Generar Boceto Técnico (Run AI)';
    }
  });

  // 7. Download Handlers
  downloadDxf.addEventListener('click', () => {
    if (downloadUrls.dxf) {
      window.location.href = downloadUrls.dxf;
    } else {
      alert('Primero debes generar el boceto técnico con la IA.');
    }
  });

  downloadSvg.addEventListener('click', () => {
    if (downloadUrls.svg) {
      window.location.href = downloadUrls.svg;
    } else {
      alert('Primero debes generar el boceto técnico con la IA.');
    }
  });

  downloadPng.addEventListener('click', () => {
    if (downloadUrls.png) {
      window.location.href = downloadUrls.png;
    } else {
      alert('Primero debes generar el boceto técnico con la IA.');
    }
  });
});
