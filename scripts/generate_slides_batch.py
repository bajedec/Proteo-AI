"""
scripts/generate_slides_batch.py
================================
Genera el archivo JSON con todas las operaciones batch para construir las
diapositivas 2 a 10 en Google Slides para la exposición de Proteo AI.
"""

import json

slides_ops = []

# --- SLIDE 2: Arquitectura del Sistema & Desacoplamiento Frontend ---
slides_ops.extend([
    {"op": "add-slide", "id": "SLIDE_2"},
    {"op": "set-background", "slide": "SLIDE_2", "color": "#0B132B"},
    {
        "op": "add-textbox",
        "slide": "SLIDE_2",
        "text": "ARQUITECTURA DE SOFTWARE",
        "x": 40, "y": 25, "width": 640, "height": 18,
        "font_size": 10, "bold": True, "color": "#94A3B8"
    },
    {
        "op": "add-textbox",
        "slide": "SLIDE_2",
        "text": "Desacoplamiento Frontend & Arquitectura del Sistema",
        "x": 40, "y": 45, "width": 640, "height": 35,
        "font_size": 20, "bold": True, "color": "#38BDF8"
    },
    # Card 1
    {
        "op": "add-textbox",
        "slide": "SLIDE_2",
        "text": "1. Desacoplamiento Ágil\n\n• El Frontend opera con total autonomía sin depender del archivo pesado del modelo de IA (model.onnx).\n\n• Permite iterar la interfaz, validar flujos y ejecutar pruebas continuas sin bloquear el desarrollo del equipo.\n\n• Simula la vectorización con algoritmos nativos (Canny + RDP).",
        "x": 40, "y": 95, "width": 200, "height": 240,
        "font_size": 10.5, "color": "#E2E8F0",
        "background_color": "#1E293B",
        "outline_color": "#334155", "outline_weight": 1.0
    },
    # Card 2
    {
        "op": "add-textbox",
        "slide": "SLIDE_2",
        "text": "2. Stack Tecnológico\n\n• FastAPI (Python 3.11): Backend asíncrono de alto rendimiento.\n\n• Starlette Templates: Renderizado Jinja2 modular.\n\n• Google Stitch UI: Diseño moderno con Tailwind CSS (Dark CAD).\n\n• OpenCV & ezdxf: Procesamiento de imágenes y generación AutoCAD R2010.",
        "x": 260, "y": 95, "width": 200, "height": 240,
        "font_size": 10.5, "color": "#E2E8F0",
        "background_color": "#1E293B",
        "outline_color": "#0284C7", "outline_weight": 1.5
    },
    # Card 3
    {
        "op": "add-textbox",
        "slide": "SLIDE_2",
        "text": "3. Flujo REST Asíncrono\n\n• GET /: Carga de la vista principal e interactiva.\n\n• POST /api/process: Recepción de imagen, validación de tipo/tamaño y vectorización poligonal.\n\n• GET /api/download/{f}: Descarga segura de archivos generados (.dxf y .svg).",
        "x": 480, "y": 95, "width": 200, "height": 240,
        "font_size": 10.5, "color": "#E2E8F0",
        "background_color": "#1E293B",
        "outline_color": "#334155", "outline_weight": 1.0
    },
    # Tagline
    {
        "op": "add-textbox",
        "slide": "SLIDE_2",
        "text": "Principio arquitectónico: Modularidad y separación de responsabilidades entre Frontend y Modelo de IA.",
        "x": 40, "y": 355, "width": 640, "height": 22,
        "font_size": 9.5, "italic": True, "color": "#64748B", "alignment": "center"
    },
    {
        "op": "set-notes",
        "slide": "SLIDE_2",
        "text": "GUION DE EXPOSICIÓN (MINUTOS 1:30 - 3:30):\nComo desarrollador Frontend, una de las decisiones arquitectónicas fundamentales fue desacoplar completamente la capa visual y de endpoints de los pesos pesados del modelo de IA (model.onnx). ¿Por qué? Porque un modelo de deep learning en entrenamiento pesa cientos de megabytes y puede tardar días en optimizarse. Gracias al desacoplamiento, hemos construido una suite funcional en FastAPI donde el usuario puede subir planos, calibrar tolerancias, previsualizar resultados y descargar archivos DXF/SVG reales. Cuando el equipo de ML termine de afinar el modelo ONNX, la integración será transparente sin necesidad de tocar una sola línea del frontend."
    }
])

# --- SLIDE 3: Frontend Operativo (Google Stitch CAD UI) ---
slides_ops.extend([
    {"op": "add-slide", "id": "SLIDE_3"},
    {"op": "set-background", "slide": "SLIDE_3", "color": "#0B132B"},
    {
        "op": "add-textbox",
        "slide": "SLIDE_3",
        "text": "EXPERIENCIA DE USUARIO & INTERFAZ",
        "x": 40, "y": 25, "width": 640, "height": 18,
        "font_size": 10, "bold": True, "color": "#94A3B8"
    },
    {
        "op": "add-textbox",
        "slide": "SLIDE_3",
        "text": "Frontend Operativo: Google Stitch CAD UI",
        "x": 40, "y": 45, "width": 640, "height": 35,
        "font_size": 20, "bold": True, "color": "#38BDF8"
    },
    # Card 1
    {
        "op": "add-textbox",
        "slide": "SLIDE_3",
        "text": "Drag & Drop Nativo\n\n• Implementado con la API nativa HTML5 FileReader.\n\n• Proyección inmediata en lienzo izquierdo (memoria local) sin esperar la respuesta del servidor.\n\n• Validación de extensiones permitidas (.png, .jpg, .jpeg) y bloqueo de formatos no válidos.",
        "x": 40, "y": 95, "width": 200, "height": 240,
        "font_size": 10.5, "color": "#E2E8F0",
        "background_color": "#1E293B",
        "outline_color": "#334155", "outline_weight": 1.0
    },
    # Card 2
    {
        "op": "add-textbox",
        "slide": "SLIDE_3",
        "text": "Calibración Reactiva\n\n• Sliders con retroalimentación en tiempo real:\n  - Grosor de Trazo (1.00 a 5.00 pt).\n  - Tolerancia RDP (ε = 0.50 a 5.00).\n\n• Presets de estilo de un clic:\n  - Estilo CAD Industrial.\n  - Boceto Mínimo.\n  - Trazo Manga / Artístico.",
        "x": 260, "y": 95, "width": 200, "height": 240,
        "font_size": 10.5, "color": "#E2E8F0",
        "background_color": "#1E293B",
        "outline_color": "#0284C7", "outline_weight": 1.5
    },
    # Card 3
    {
        "op": "add-textbox",
        "slide": "SLIDE_3",
        "text": "Telemetría HUD & Exportación\n\n• Cápsula de telemetría HUD en tiempo real:\n  - Latencia exacta de procesamiento en milisegundos.\n  - Conteo de entidades y polilíneas CAD generadas.\n\n• Descarga con un clic:\n  - AutoCAD DXF (R2010 nativo).\n  - W3C SVG vectorial escalable.",
        "x": 480, "y": 95, "width": 200, "height": 240,
        "font_size": 10.5, "color": "#E2E8F0",
        "background_color": "#1E293B",
        "outline_color": "#334155", "outline_weight": 1.0
    },
    {
        "op": "add-textbox",
        "slide": "SLIDE_3",
        "text": "Interfaz oscura profesional inspirada en estaciones de trabajo de ingeniería y arquitectura.",
        "x": 40, "y": 355, "width": 640, "height": 22,
        "font_size": 9.5, "italic": True, "color": "#64748B", "alignment": "center"
    },
    {
        "op": "set-notes",
        "slide": "SLIDE_3",
        "text": "GUION DE EXPOSICIÓN (MINUTOS 3:30 - 6:00):\nAquí vemos la interfaz Google Stitch CAD UI. Como Frontend Developer, me enfoqué en que la experiencia de usuario fuera inmediata y robusta. Al arrastrar una imagen, el navegador la lee con la API FileReader y la proyecta al instante en memoria. Los controles deslizantes permiten calibrar la precisión del algoritmo Ramer-Douglas-Peucker (epsilon) para simplificar contornos antes de exportar. El HUD superior muestra telemetría real: tiempo de respuesta en milisegundos y número de polilíneas. Y los botones de exportación generan archivos DXF estándar de AutoCAD compatibles con cualquier versión comercial."
    }
])

# --- SLIDE 4: Matriz de Cumplimiento de la Rúbrica (20 / 20 pts) ---
slides_ops.extend([
    {"op": "add-slide", "id": "SLIDE_4"},
    {"op": "set-background", "slide": "SLIDE_4", "color": "#0B132B"},
    {
        "op": "add-textbox",
        "slide": "SLIDE_4",
        "text": "EVALUACIÓN CONSOLIDADO 2 • RÚBRICA CONTINENTAL",
        "x": 40, "y": 25, "width": 640, "height": 18,
        "font_size": 10, "bold": True, "color": "#94A3B8"
    },
    {
        "op": "add-textbox",
        "slide": "SLIDE_4",
        "text": "Matriz de Cumplimiento: Rúbrica Oficial (20 / 20 pts)",
        "x": 40, "y": 45, "width": 640, "height": 35,
        "font_size": 20, "bold": True, "color": "#38BDF8"
    },
    # Tabla con los criterios
    {
        "op": "add-table",
        "slide": "SLIDE_4",
        "rows": 5, "cols": 4,
        "id": "TABLE_RUBRICA",
        "x": 40, "y": 90, "width": 640, "height": 230
    },
    # Header tabla
    {"op": "set-table-cell", "table": "TABLE_RUBRICA", "row": 0, "col": 0, "text": "CRITERIO / SEMANA", "bold": True, "color": "#FFFFFF", "background_color": "#0F172A", "font_size": 9.5},
    {"op": "set-table-cell", "table": "TABLE_RUBRICA", "row": 0, "col": 1, "text": "MÁX.", "bold": True, "color": "#FFFFFF", "background_color": "#0F172A", "font_size": 9.5},
    {"op": "set-table-cell", "table": "TABLE_RUBRICA", "row": 0, "col": 2, "text": "ESTADO", "bold": True, "color": "#FFFFFF", "background_color": "#0F172A", "font_size": 9.5},
    {"op": "set-table-cell", "table": "TABLE_RUBRICA", "row": 0, "col": 3, "text": "EVIDENCIA TÉCNICA EN EL REPOSITORIO", "bold": True, "color": "#FFFFFF", "background_color": "#0F172A", "font_size": 9.5},
    # Row 1: S9
    {"op": "set-table-cell", "table": "TABLE_RUBRICA", "row": 1, "col": 0, "text": "S9: Tests Unitarios y Estructura", "color": "#E2E8F0", "font_size": 9, "background_color": "#1E293B"},
    {"op": "set-table-cell", "table": "TABLE_RUBRICA", "row": 1, "col": 1, "text": "5 pts", "color": "#38BDF8", "bold": True, "font_size": 9, "background_color": "#1E293B"},
    {"op": "set-table-cell", "table": "TABLE_RUBRICA", "row": 1, "col": 2, "text": "5 pts (Excelente)", "color": "#10B981", "bold": True, "font_size": 9, "background_color": "#1E293B"},
    {"op": "set-table-cell", "table": "TABLE_RUBRICA", "row": 1, "col": 3, "text": "28 tests en tests/test_*.py con unittest.TestCase cubriendo tipos y límites.", "color": "#E2E8F0", "font_size": 8.5, "background_color": "#1E293B"},
    # Row 2: S10
    {"op": "set-table-cell", "table": "TABLE_RUBRICA", "row": 2, "col": 0, "text": "S10: Metodología TDD", "color": "#E2E8F0", "font_size": 9, "background_color": "#0F172A"},
    {"op": "set-table-cell", "table": "TABLE_RUBRICA", "row": 2, "col": 1, "text": "5 pts", "color": "#38BDF8", "bold": True, "font_size": 9, "background_color": "#0F172A"},
    {"op": "set-table-cell", "table": "TABLE_RUBRICA", "row": 2, "col": 2, "text": "5 pts (Excelente)", "color": "#10B981", "bold": True, "font_size": 9, "background_color": "#0F172A"},
    {"op": "set-table-cell", "table": "TABLE_RUBRICA", "row": 2, "col": 3, "text": "Doble ciclo Red-Green-Refactor en commits (tamano_archivo y tolerancia_rdp).", "color": "#E2E8F0", "font_size": 8.5, "background_color": "#0F172A"},
    # Row 3: S11a
    {"op": "set-table-cell", "table": "TABLE_RUBRICA", "row": 3, "col": 0, "text": "S11: Cobertura de Código (≥ 60%)", "color": "#E2E8F0", "font_size": 9, "background_color": "#1E293B"},
    {"op": "set-table-cell", "table": "TABLE_RUBRICA", "row": 3, "col": 1, "text": "5 pts", "color": "#38BDF8", "bold": True, "font_size": 9, "background_color": "#1E293B"},
    {"op": "set-table-cell", "table": "TABLE_RUBRICA", "row": 3, "col": 2, "text": "5 pts (Excelente)", "color": "#10B981", "bold": True, "font_size": 9, "background_color": "#1E293B"},
    {"op": "set-table-cell", "table": "TABLE_RUBRICA", "row": 3, "col": 3, "text": ".coveragerc con fail_under=60; 92% de cobertura global y reporte htmlcov/.", "color": "#E2E8F0", "font_size": 8.5, "background_color": "#1E293B"},
    # Row 4: S11b
    {"op": "set-table-cell", "table": "TABLE_RUBRICA", "row": 4, "col": 0, "text": "S11: CI/CD y Refactoring", "color": "#E2E8F0", "font_size": 9, "background_color": "#0F172A"},
    {"op": "set-table-cell", "table": "TABLE_RUBRICA", "row": 4, "col": 1, "text": "5 pts", "color": "#38BDF8", "bold": True, "font_size": 9, "background_color": "#0F172A"},
    {"op": "set-table-cell", "table": "TABLE_RUBRICA", "row": 4, "col": 2, "text": "5 pts (Excelente)", "color": "#10B981", "bold": True, "font_size": 9, "background_color": "#0F172A"},
    {"op": "set-table-cell", "table": "TABLE_RUBRICA", "row": 4, "col": 3, "text": "GitHub Actions en .github/workflows/ci.yml y 0 números mágicos en app.py.", "color": "#E2E8F0", "font_size": 8.5, "background_color": "#0F172A"},
    # Callout
    {
        "op": "add-textbox",
        "slide": "SLIDE_4",
        "text": "CALIFICACIÓN TOTAL PROYECTADA: 20 / 20 PUNTOS (100% de cumplimiento en rúbrica oficial)",
        "x": 40, "y": 335, "width": 640, "height": 35,
        "font_size": 11, "bold": True, "color": "#10B981",
        "background_color": "#064E3B",
        "outline_color": "#10B981", "outline_weight": 1.5,
        "alignment": "center"
    },
    {
        "op": "set-notes",
        "slide": "SLIDE_4",
        "text": "GUION DE EXPOSICIÓN (MINUTOS 6:00 - 8:30):\nEstimado docente Ing. Henderson, hemos alineado cada línea de desarrollo con la rúbrica oficial de la evaluación. Como puede apreciar en esta matriz de trazabilidad: para S9 tenemos 28 tests con unittest.TestCase cubriendo límites y excepciones; para S10 demostramos la metodología TDD con commits estructurados en Red-Green-Refactor; para S11 superamos ampliamente el 60% requerido alcanzando un 92% de cobertura con .coveragerc configurado; y para CI/CD tenemos el pipeline de GitHub Actions activo y el código totalmente refactorizado sin números mágicos. La calificación obtenida en todos los criterios es Excelente (20/20)."
    }
])

# --- SLIDE 5: Metodología TDD (Ciclo Red-Green-Refactor) ---
slides_ops.extend([
    {"op": "add-slide", "id": "SLIDE_5"},
    {"op": "set-background", "slide": "SLIDE_5", "color": "#0B132B"},
    {
        "op": "add-textbox",
        "slide": "SLIDE_5",
        "text": "METODOLOGÍA DE DESARROLLO (CRITERIO S10)",
        "x": 40, "y": 25, "width": 640, "height": 18,
        "font_size": 10, "bold": True, "color": "#94A3B8"
    },
    {
        "op": "add-textbox",
        "slide": "SLIDE_5",
        "text": "Metodología TDD: Ciclo Red-Green-Refactor en Commits",
        "x": 40, "y": 45, "width": 640, "height": 35,
        "font_size": 20, "bold": True, "color": "#38BDF8"
    },
    # Card RED
    {
        "op": "add-textbox",
        "slide": "SLIDE_5",
        "text": "FASE [RED]: Test Primero\n\n• Se redacta la prueba unitaria antes de escribir la función en producción.\n\n• El test falla en rojo comprobando que la aserción es efectiva.\n\n• Commit 1b4269b (Saul):\ntest: [RED] pruebas tamano archivo.\n\n• Commit 01a973a (Oscar):\ntest: [RED] pruebas tolerancia rdp.",
        "x": 40, "y": 95, "width": 200, "height": 240,
        "font_size": 10, "color": "#FCA5A5",
        "background_color": "#450A0A",
        "outline_color": "#EF4444", "outline_weight": 1.5
    },
    # Card GREEN
    {
        "op": "add-textbox",
        "slide": "SLIDE_5",
        "text": "FASE [GREEN]: Código Mínimo\n\n• Se implementa la lógica mínima necesaria para hacer pasar las pruebas.\n\n• Toda la suite cambia a verde.\n\n• Commit 73aa1cc (Saul):\nfeat: [GREEN] implementar validar_tamano_archivo.\n\n• Commit 0455c8f (Oscar):\nfeat: [GREEN] implementar validar_tolerancia_rdp.",
        "x": 260, "y": 95, "width": 200, "height": 240,
        "font_size": 10, "color": "#A7F3D0",
        "background_color": "#064E3B",
        "outline_color": "#10B981", "outline_weight": 1.5
    },
    # Card REFACTOR
    {
        "op": "add-textbox",
        "slide": "SLIDE_5",
        "text": "FASE [REFACTOR]: Limpieza\n\n• Se optimiza el diseño y se eliminan duplicaciones sin romper los tests.\n\n• Commit 10db2ec (Saul):\nrefactor: parametrizar con self.subTest(...) en 5 rangos de tamaño.\n\n• Commit 30ab603 (Oscar):\nrefactor: extracción de constantes RDP_EPSILON_MIN y MAX.",
        "x": 480, "y": 95, "width": 200, "height": 240,
        "font_size": 10, "color": "#BAE6FD",
        "background_color": "#0C4A6E",
        "outline_color": "#0284C7", "outline_weight": 1.5
    },
    {
        "op": "add-textbox",
        "slide": "SLIDE_5",
        "text": "El árbol de Git registra dos ciclos completos de TDD desarrollados de forma colaborativa.",
        "x": 40, "y": 355, "width": 640, "height": 22,
        "font_size": 9.5, "italic": True, "color": "#64748B", "alignment": "center"
    },
    {
        "op": "set-notes",
        "slide": "SLIDE_5",
        "text": "GUION DE EXPOSICIÓN (MINUTOS 8:30 - 11:00):\nEl criterio S10 exige evidencia fehaciente de TDD en los commits. En nuestro repositorio no escribimos los tests al final; el historial de Git prueba que seguimos el ciclo estricto Red-Green-Refactor. Por ejemplo, en mi trabajo de Frontend, el commit 1b4269b introdujo la prueba para el tamaño de archivo antes de existir la función; el commit 73aa1cc escribió el código mínimo que pasó los tests a verde; y el commit 10db2ec refactorizó la prueba usando subTest de unittest para evaluar 5 rangos distintos de tamaño sin duplicar código. Mi compañero Oscar aplicó idéntica disciplina en la tolerancia RDP."
    }
])

# --- SLIDE 6: Refactorización Arquitectónica & Eliminación de Números Mágicos ---
slides_ops.extend([
    {"op": "add-slide", "id": "SLIDE_6"},
    {"op": "set-background", "slide": "SLIDE_6", "color": "#0B132B"},
    {
        "op": "add-textbox",
        "slide": "SLIDE_6",
        "text": "REFACTORIZACIÓN DE CÓDIGO (CRITERIO S11)",
        "x": 40, "y": 25, "width": 640, "height": 18,
        "font_size": 10, "bold": True, "color": "#94A3B8"
    },
    {
        "op": "add-textbox",
        "slide": "SLIDE_6",
        "text": "Refactorización: Erradicación de Números Mágicos",
        "x": 40, "y": 45, "width": 640, "height": 35,
        "font_size": 20, "bold": True, "color": "#38BDF8"
    },
    # Card Antes
    {
        "op": "add-textbox",
        "slide": "SLIDE_6",
        "text": "ANTES (Código con Números Mágicos)\n\n• cv2.Canny(gray, 50, 150, apertureSize=3)\n  → ¿Qué significan 50 y 150?\n\n• if cv2.contourArea(c) < 20:\n  → 20 quemado en medio del código.\n\n• doc.header['$INSUNITS'] = 4\n  → 4 hardcodeado sin documentación.\n\n• stroke_width = 1.0\n  → Valor arbitrario difícil de mantener.",
        "x": 40, "y": 95, "width": 305, "height": 235,
        "font_size": 10.5, "color": "#FCA5A5",
        "background_color": "#1E293B",
        "outline_color": "#EF4444", "outline_weight": 1.5
    },
    # Card Después
    {
        "op": "add-textbox",
        "slide": "SLIDE_6",
        "text": "DESPUÉS (Refactorizado en commit 420f38e)\n\n• CANNY_LOW_DEFAULT = 50\n• CANNY_HIGH_DEFAULT = 150\n• CANNY_APERTURE_SIZE = 3\n• CONTOUR_AREA_MIN = 20\n• DXF_HEADER_VERSION = 'AC1024'\n• DXF_UNITS_MILLIMETERS = 4\n• SVG_STROKE_WIDTH_DEFAULT = 1.0\n• RDP_EPSILON_MIN = 0.1, RDP_EPSILON_MAX = 10.0",
        "x": 375, "y": 95, "width": 305, "height": 235,
        "font_size": 10.5, "color": "#A7F3D0",
        "background_color": "#1E293B",
        "outline_color": "#10B981", "outline_weight": 1.5
    },
    {
        "op": "add-textbox",
        "slide": "SLIDE_6",
        "text": "Resultado: 0 números mágicos en src/app.py y adherencia estricta a Clean Code.",
        "x": 40, "y": 355, "width": 640, "height": 22,
        "font_size": 9.5, "italic": True, "color": "#64748B", "alignment": "center"
    },
    {
        "op": "set-notes",
        "slide": "SLIDE_6",
        "text": "GUION DE EXPOSICIÓN (MINUTOS 11:00 - 13:00):\nEl criterio de refactorización de la semana 11 exige código limpio y libre de números mágicos. En la pantalla izquierda vemos cómo estaba inicialmente: umbrales de 50 y 150 en Canny, tamaños mínimos de área de 20 píxeles y códigos de unidad de AutoCAD como el número 4 hardcodeados. En el commit 420f38e realizamos una refactorización integral: extrajimos todas estas cifras a constantes semánticas en mayúsculas en la cabecera de src/app.py. Esto no solo cumple la rúbrica al 100%, sino que hace que el sistema sea configurable y auto-documentado."
    }
])

# --- SLIDE 7: Cobertura de Código y .coveragerc ---
slides_ops.extend([
    {"op": "add-slide", "id": "SLIDE_7"},
    {"op": "set-background", "slide": "SLIDE_7", "color": "#0B132B"},
    {
        "op": "add-textbox",
        "slide": "SLIDE_7",
        "text": "COBERTURA DE PRUEBAS (CRITERIO S11)",
        "x": 40, "y": 25, "width": 640, "height": 18,
        "font_size": 10, "bold": True, "color": "#94A3B8"
    },
    {
        "op": "add-textbox",
        "slide": "SLIDE_7",
        "text": "Cobertura de Pruebas: 92% Global (Excede ≥ 60%)",
        "x": 40, "y": 45, "width": 640, "height": 35,
        "font_size": 20, "bold": True, "color": "#38BDF8"
    },
    # 4 Stat Boxes
    {
        "op": "add-textbox",
        "slide": "SLIDE_7",
        "text": "92%\nCOBERTURA GLOBAL",
        "x": 40, "y": 95, "width": 145, "height": 65,
        "font_size": 18, "bold": True, "color": "#10B981",
        "background_color": "#1E293B", "outline_color": "#10B981", "outline_weight": 1.5,
        "alignment": "center"
    },
    {
        "op": "add-textbox",
        "slide": "SLIDE_7",
        "text": "28 / 28\nTESTS PASANDO",
        "x": 205, "y": 95, "width": 145, "height": 65,
        "font_size": 18, "bold": True, "color": "#38BDF8",
        "background_color": "#1E293B", "outline_color": "#0284C7", "outline_weight": 1.5,
        "alignment": "center"
    },
    {
        "op": "add-textbox",
        "slide": "SLIDE_7",
        "text": "100%\nVALIDADORES.PY",
        "x": 370, "y": 95, "width": 145, "height": 65,
        "font_size": 18, "bold": True, "color": "#F59E0B",
        "background_color": "#1E293B", "outline_color": "#F59E0B", "outline_weight": 1.5,
        "alignment": "center"
    },
    {
        "op": "add-textbox",
        "slide": "SLIDE_7",
        "text": "0.75s\nTIEMPO DE SUITE",
        "x": 535, "y": 95, "width": 145, "height": 65,
        "font_size": 18, "bold": True, "color": "#A855F7",
        "background_color": "#1E293B", "outline_color": "#A855F7", "outline_weight": 1.5,
        "alignment": "center"
    },
    # Configuración de .coveragerc
    {
        "op": "add-textbox",
        "slide": "SLIDE_7",
        "text": "Configuración Formal de .coveragerc\n\n[run]\nsource = src\nomit =\n    tests/*\n    venv/*\n\n[report]\nfail_under = 60\nshow_missing = True",
        "x": 40, "y": 180, "width": 310, "height": 160,
        "font_size": 10.5, "color": "#E2E8F0",
        "background_color": "#0F172A", "outline_color": "#334155", "outline_weight": 1.0
    },
    # Explicación
    {
        "op": "add-textbox",
        "slide": "SLIDE_7",
        "text": "Garantías de Calidad Implementadas:\n\n• fail_under = 60: Rompe la compilación si la cobertura cae al 59%.\n\n• show_missing = True: Reporta líneas no alcanzadas para mejora continua.\n\n• Reporte HTML: Carpeta htmlcov/ index.html generada para auditoría visual.\n\n• 0 errores de linteo en flake8 con límite de 120 caracteres.",
        "x": 370, "y": 180, "width": 310, "height": 160,
        "font_size": 10.5, "color": "#E2E8F0",
        "background_color": "#1E293B", "outline_color": "#0284C7", "outline_weight": 1.0
    },
    {
        "op": "add-textbox",
        "slide": "SLIDE_7",
        "text": "El proyecto supera con creces el umbral mínimo del 60% exigido por la Universidad Continental.",
        "x": 40, "y": 355, "width": 640, "height": 22,
        "font_size": 9.5, "italic": True, "color": "#64748B", "alignment": "center"
    },
    {
        "op": "set-notes",
        "slide": "SLIDE_7",
        "text": "GUION DE EXPOSICIÓN (MINUTOS 13:00 - 15:30):\nPara el criterio S11 de cobertura, la rúbrica pide configurar .coveragerc con source, omit y fail_under, requiriendo un mínimo de 60%. En Proteo AI no solo cumplimos el mínimo, sino que alcanzamos un 92% de cobertura global. Tenemos 28 pruebas unitarias e integración que ejecutan en tan solo 0.75 segundos: el módulo src/validadores.py tiene cobertura perfecta del 100% y src/app.py alcanza el 89%. Si alguien reduce la cobertura o rompe una prueba, el archivo .coveragerc detiene inmediatamente la ejecución con código de error."
    }
])

# --- SLIDE 8: Pipeline CI/CD en GitHub Actions ---
slides_ops.extend([
    {"op": "add-slide", "id": "SLIDE_8"},
    {"op": "set-background", "slide": "SLIDE_8", "color": "#0B132B"},
    {
        "op": "add-textbox",
        "slide": "SLIDE_8",
        "text": "INTEGRACIÓN CONTINUA (CRITERIO S11)",
        "x": 40, "y": 25, "width": 640, "height": 18,
        "font_size": 10, "bold": True, "color": "#94A3B8"
    },
    {
        "op": "add-textbox",
        "slide": "SLIDE_8",
        "text": "Pipeline CI/CD Automatizado en GitHub Actions",
        "x": 40, "y": 45, "width": 640, "height": 35,
        "font_size": 20, "bold": True, "color": "#38BDF8"
    },
    # 3 Steps Cards
    {
        "op": "add-textbox",
        "slide": "SLIDE_8",
        "text": "1. Triggers de Eventos\n\n• Activación automática ante cualquier:\n  - push hacia main y develop.\n  - pull_request hacia main.\n\n• Aislamiento en máquina virtual Ubuntu (ubuntu-latest).",
        "x": 40, "y": 95, "width": 200, "height": 240,
        "font_size": 10.5, "color": "#E2E8F0",
        "background_color": "#1E293B",
        "outline_color": "#334155", "outline_weight": 1.0
    },
    {
        "op": "add-textbox",
        "slide": "SLIDE_8",
        "text": "2. Matriz de Entorno\n\n• actions/checkout@v4.\n\n• actions/setup-python@v5 con versión oficial Python 3.11.\n\n• Instalación de librerías desde requirements.txt en caché para máxima velocidad.",
        "x": 260, "y": 95, "width": 200, "height": 240,
        "font_size": 10.5, "color": "#E2E8F0",
        "background_color": "#1E293B",
        "outline_color": "#0284C7", "outline_weight": 1.5
    },
    {
        "op": "add-textbox",
        "slide": "SLIDE_8",
        "text": "3. Quality Gatekeeper\n\n• Linter PEP8:\nflake8 src/ tests/ --max-line-length=120\n\n• Ejecución de Tests:\ncoverage run -m unittest discover\n\n• Verificación de Cobertura:\ncoverage report --fail-under=60\ncoverage html",
        "x": 480, "y": 95, "width": 200, "height": 240,
        "font_size": 10, "color": "#A7F3D0",
        "background_color": "#064E3B",
        "outline_color": "#10B981", "outline_weight": 1.5
    },
    {
        "op": "add-textbox",
        "slide": "SLIDE_8",
        "text": "Configurado en .github/workflows/ci.yml: Garantiza que ningún commit con errores ingrese a main.",
        "x": 40, "y": 355, "width": 640, "height": 22,
        "font_size": 9.5, "italic": True, "color": "#64748B", "alignment": "center"
    },
    {
        "op": "set-notes",
        "slide": "SLIDE_8",
        "text": "GUION DE EXPOSICIÓN (MINUTOS 15:30 - 17:30):\nEn cuanto al pipeline CI/CD, configuramos el archivo .github/workflows/ci.yml. Cada vez que cualquier integrante del equipo hace un push o abre un pull request, los runners de GitHub instancian un contenedor Ubuntu con Python 3.11, instalan dependencias y ejecutan las pruebas unitarias y el reporte de cobertura con fail-under=60. Si un desarrollador sube código con un test roto o que baje la cobertura, el build se pone en rojo y GitHub bloquea la integración. Esto garantiza estabilidad continua en la rama principal."
    }
])

# --- SLIDE 9: Gestión Colaborativa del Repositorio (Git Tree) ---
slides_ops.extend([
    {"op": "add-slide", "id": "SLIDE_9"},
    {"op": "set-background", "slide": "SLIDE_9", "color": "#0B132B"},
    {
        "op": "add-textbox",
        "slide": "SLIDE_9",
        "text": "GESTIÓN COLABORATIVA & TRABAJO EN EQUIPO",
        "x": 40, "y": 25, "width": 640, "height": 18,
        "font_size": 10, "bold": True, "color": "#94A3B8"
    },
    {
        "op": "add-textbox",
        "slide": "SLIDE_9",
        "text": "Gestión Colaborativa del Repositorio (Git Tree)",
        "x": 40, "y": 45, "width": 640, "height": 35,
        "font_size": 20, "bold": True, "color": "#38BDF8"
    },
    # Card Izquierda: Integrantes
    {
        "op": "add-textbox",
        "slide": "SLIDE_9",
        "text": "Contribuciones del Equipo 'Baje de C++'\n\n• Saul Huillca (74401464 - Frontend Developer):\n  - Arquitectura Stitch UI y templates Jinja2.\n  - Endpoints REST en FastAPI (/ y /api/process).\n  - Ciclo TDD en validar_tamano_archivo con subTest.\n  - Elevación de cobertura al 92% y 0 errores flake8.\n\n• Oscar (73138388):\n  - Ciclo TDD en validar_tolerancia_rdp.\n  - Erradicación de números mágicos en src/app.py.\n\n• Florbyte (71632278):\n  - Refinamiento de aserciones en test_frontend.py.",
        "x": 40, "y": 95, "width": 305, "height": 240,
        "font_size": 10, "color": "#E2E8F0",
        "background_color": "#1E293B",
        "outline_color": "#0284C7", "outline_weight": 1.5
    },
    # Card Derecha: Buenas Prácticas
    {
        "op": "add-textbox",
        "slide": "SLIDE_9",
        "text": "Disciplina de Control de Versiones\n\n• Archivo AGENTS.md:\n  - Institucionalizado en la raíz del repositorio.\n  - Fija la regla de ≥ 60% cobertura y linteo PEP8.\n  - Protege el desacoplamiento entre frontend e IA.\n\n• Manejo de Conflictos y Rebase:\n  - Sincronización continua con git pull --rebase.\n  - Resolución limpia de colisiones en validadores.\n  - Mensajes de commit con etiquetas semánticas:\n    feat:, test: [RED], feat: [GREEN], refactor:.",
        "x": 375, "y": 95, "width": 305, "height": 240,
        "font_size": 10, "color": "#E2E8F0",
        "background_color": "#1E293B",
        "outline_color": "#334155", "outline_weight": 1.0
    },
    {
        "op": "add-textbox",
        "slide": "SLIDE_9",
        "text": "El repositorio se encuentra limpio, actualizado y sincronizado en la rama main.",
        "x": 40, "y": 355, "width": 640, "height": 22,
        "font_size": 9.5, "italic": True, "color": "#64748B", "alignment": "center"
    },
    {
        "op": "set-notes",
        "slide": "SLIDE_9",
        "text": "GUION DE EXPOSICIÓN (MINUTOS 17:30 - 19:00):\nComo equipo Baje de C++, hemos trabajado de forma colaborativa y sincronizada. En mi rol como Frontend Developer, me aseguré de que la interfaz y los endpoints estuvieran blindados por pruebas. Mis compañeros Oscar y Florbyte aportaron en la refactorización y pruebas adicionales. Institucionalizamos un archivo AGENTS.md en el repositorio para que todo el equipo respete los estándares de cobertura y linteo. Hemos manejado las ramas con commits semánticos y sincronización constante, manteniendo la rama main en verde."
    }
])

# --- SLIDE 10: Conclusiones y Próxima Fase ---
slides_ops.extend([
    {"op": "add-slide", "id": "SLIDE_10"},
    {"op": "set-background", "slide": "SLIDE_10", "color": "#0B132B"},
    {
        "op": "add-textbox",
        "slide": "SLIDE_10",
        "text": "CONCLUSIONES & HOJA DE RUTA",
        "x": 40, "y": 25, "width": 640, "height": 18,
        "font_size": 10, "bold": True, "color": "#94A3B8"
    },
    {
        "op": "add-textbox",
        "slide": "SLIDE_10",
        "text": "Conclusiones y Hoja de Ruta para la Entrega Final",
        "x": 40, "y": 45, "width": 640, "height": 35,
        "font_size": 20, "bold": True, "color": "#38BDF8"
    },
    # Card 1
    {
        "op": "add-textbox",
        "slide": "SLIDE_10",
        "text": "1. Objetivos Cumplidos\n\n• 100% de la rúbrica institucional lograda (20 / 20 puntos proyectados).\n\n• Frontend CAD funcional, reactivo y desacoplado.\n\n• Generación real de archivos vectoriales DXF y SVG.",
        "x": 40, "y": 95, "width": 200, "height": 230,
        "font_size": 10.5, "color": "#E2E8F0",
        "background_color": "#1E293B",
        "outline_color": "#10B981", "outline_weight": 1.5
    },
    # Card 2
    {
        "op": "add-textbox",
        "slide": "SLIDE_10",
        "text": "2. Calidad de Software\n\n• 28 pruebas unitarias pasando al 100% en menos de 0.8s.\n\n• 92% de cobertura de código con .coveragerc estricto.\n\n• Pipeline CI/CD en GitHub Actions activo y 0 errores flake8.",
        "x": 260, "y": 95, "width": 200, "height": 230,
        "font_size": 10.5, "color": "#E2E8F0",
        "background_color": "#1E293B",
        "outline_color": "#0284C7", "outline_weight": 1.5
    },
    # Card 3
    {
        "op": "add-textbox",
        "slide": "SLIDE_10",
        "text": "3. Fase Final (Consolidado 3)\n\n• Integración de los pesos pesados del modelo de IA (model.onnx).\n\n• Vectorización neuronal de planos arquitectónicos complejos.\n\n• Despliegue en producción en la nube.",
        "x": 480, "y": 95, "width": 200, "height": 230,
        "font_size": 10.5, "color": "#E2E8F0",
        "background_color": "#1E293B",
        "outline_color": "#F59E0B", "outline_weight": 1.5
    },
    # Cierre
    {
        "op": "add-textbox",
        "slide": "SLIDE_10",
        "text": "¡Muchas gracias por su atención! • Preguntas y Demostración en Vivo",
        "x": 40, "y": 340, "width": 640, "height": 35,
        "font_size": 12, "bold": True, "color": "#38BDF8",
        "background_color": "#1E293B",
        "outline_color": "#38BDF8", "outline_weight": 1.5,
        "alignment": "center"
    },
    {
        "op": "set-notes",
        "slide": "SLIDE_10",
        "text": "GUION DE EXPOSICIÓN (MINUTOS 19:00 - 20:00):\nEn conclusión, hemos alcanzado satisfactoriamente los objetivos de este avance: el frontend está completamente operativo y desacoplado, los estándares de TDD y refactorización están plasmados en el historial de Git, y la cobertura supera con un 92% la exigencia institucional. Nuestra base de software está lista para recibir el modelo ONNX en la fase final sin retrabajos. Agradecemos su tiempo, Ing. Henderson Gibaja, y quedamos atentos a sus preguntas y a la demostración en vivo de la plataforma. Muchas gracias."
    }
])

with open("scripts/batch_slides_all.json", "w", encoding="utf-8") as f:
    json.dump(slides_ops, f, indent=2, ensure_ascii=False)

print(f"Generado scripts/batch_slides_all.json con {len(slides_ops)} operaciones batch.")
