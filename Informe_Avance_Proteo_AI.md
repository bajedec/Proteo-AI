# UNIVERSIDAD CONTINENTAL
## FACULTAD DE INGENIERÍA
### INGENIERÍA DE SISTEMAS E INFORMÁTICA

---

# INFORME TÉCNICO DE AVANCE DE PROYECTO
## PROYECTO: PROTEO AI — CAD & 2D SKETCH STUDIO

- **Asignatura:** Construcción de Software
- **Docente:** Ing. Henderson Nozart Gibaja Reyes
- **Equipo de Desarrollo:** Baje de C++
- **Estudiante Responsable:** Saul Adain Huillca Rodriguez (Código: 74401464)
- **Rol Asignado:** Desarrollador Frontend
- **Fecha de Entrega:** Noviembre 2026
- **Repositorio Oficial:** [github.com/bajedec/Proteo-AI](https://github.com/bajedec/Proteo-AI)

---

## 1. RESUMEN EJECUTIVO

El presente informe detalla el progreso técnico alcanzado en el desarrollo de **Proteo AI**, una plataforma orientada a ilustradores, modeladores 3D y diseñadores que automatiza la conversión de fotografías reales de objetos, estructuras y vehículos en **bocetos 2D (Line Art) y trazados vectoriales técnicos compatibles con AutoCAD (.DXF), Blender/Web (.SVG) e imágenes de alta definición (.PNG)**.

En estricto cumplimiento con los objetivos de la etapa actual, se ha completado la construcción y prueba del **Módulo Frontend**: un cascarón funcional interactivo basado en una estación de trabajo CAD (*Aerospace Dark CAD Workstation*), desarrollado con **FastAPI, Tailwind CSS y JavaScript**, validado rigurosamente bajo la metodología **TDD (Test-Driven Development)** y alcanzando un **86% de cobertura de pruebas unitarias**, superando el umbral exigido del 60% establecido en la **Semana 11** de la asignatura.

---

## 2. PROBLEMÁTICA Y SOLUCIÓN PROPUESTA

### 2.1 El Problema
Los artistas conceptuales y modeladores 3D invierten entre 3 y 8 horas calcando manualmente fotografías de referencia para obtener planos ortogonales o siluetas limpias antes de iniciar el modelado en herramientas CAD (AutoCAD, Blender, SolidWorks). Los filtros clásicos de imagen (como Canny o Sobel sin procesamiento semántico) devuelven contornos saturados de ruido visual, texturas y sombras que resultan inservibles para la ingeniería.

### 2.2 La Solución de Proteo AI
Proteo AI implementa una arquitectura en pipeline desacoplada:
1. **Fase de Ingesta y Validación:** Sanitización de extensiones, límites de peso y resolución.
2. **Fase de Extracción Geométrica:** Transformación de la fotografía a mapa de líneas estructurales de alta precisión.
3. **Fase de Vectorización Técnica:** Conversión matemática de píxeles a entidades nativas de AutoCAD (`LWPOLYLINE`) organizadas por capas, generando salidas exportables en `.DXF`, `.SVG` y `.PNG`.

---

## 3. ALCANCE DEL ENTREGABLE: ROL DE FRONTEND (CASCARÓN FUNCIONAL)

De acuerdo con las directivas del docente para esta entrega, el objetivo consistió en materializar una **versión funcional sin el modelo pesado de Deep Learning conectado todavía**, garantizando la separación de responsabilidades:

- **Cascarón Funcional:** La interfaz web no es un boceto estático de diseño; es una aplicación cliente-servidor completamente interactiva. Permite la carga de imágenes por arrastrar y soltar (*Drag & Drop*), el ajuste paramétrico de grosor de trazo y simplificación angular, y simula en milisegundos el ciclo de procesamiento y descarga.
- **Desacoplamiento de Roles:** El módulo Frontend deja definidas las rutas de consumo de la API REST (`/api/process` y `/api/download/{filename}`), dejando los módulos `src/model.py` y `training/` limpios y disponibles para que los desarrolladores de Backend y Machine Learning incorporen el modelo final entrenado sin tener que rediseñar la interfaz de usuario.

---

## 4. ESTACIÓN DE TRABAJO CAD: INTEGRACIÓN DE GOOGLE STITCH

La interfaz fue concebida en **Google Stitch** bajo el concepto de *Telemetry & Aerospace CAD Console* y trasladada al repositorio oficial con las siguientes características:

1. **Panel de Ingesta (Izquierda):**
   - Zona reactiva de arrastrar y soltar con validación en tiempo de ejecución.
   - Switch de preprocesamiento para aislar el sujeto y remover gradientes de fondo.
   - Selector de estilo de topología: *Plano CAD*, *Mínimo* y *Manga Ink*.
   - Controles deslizantes (*Sliders*) para calibrar el grosor del trazo y la tolerancia del algoritmo Ramer-Douglas-Peucker ($\epsilon$).

2. **Visor Central Dual (Viewport):**
   - Modos de visualización: comparativa lado a lado (*Side-by-Side*) y vista de trazo único.
   - Lienzo izquierdo para la imagen rasterizada original y lienzo derecho para el plano técnico vectorial.
   - Cápsula flotante de telemetría (HUD) que muestra en tiempo real la latencia de procesamiento, cantidad de polilíneas generadas y estado del sistema.

3. **Centro de Exportación Bento (Inferior):**
   - **Tarjeta 1 — AutoCAD .DXF:** Descarga directa de archivos CAD R2010 con capas asignadas (`PROTEO_TRAZOS`).
   - **Tarjeta 2 — Vector .SVG:** Descarga de gráficos vectoriales escalables con coordenadas Bezier, listo para Blender Grease Pencil o Illustrator.
   - **Tarjeta 3 — Boceto .PNG:** Descarga del arte lineal en mapa de bits de 300 DPI.

---

## 5. INGENIERÍA DE CALIDAD Y SEMANA 11 (TDD, REFACTORING Y CLEAN CODE)

El código desarrollado refleja estrictamente las enseñanzas de la **Semana 11: Cobertura de Código y Refactoring**:

### 5.1 Técnicas de Refactoring Aplicadas
- **Extract Constant:** Se erradicaron los números mágicos en `src/validadores.py` y `src/app.py`, centralizando constantes globales en mayúsculas (`LONGITUD_MINIMA_PROMPT = 3`, `LONGITUD_MAXIMA_PROMPT = 300`, `EXTENSIONES_PERMITIDAS = ('.png', '.jpg', '.jpeg')`).
- **Single Responsibility Principle (SRP):** Cada función y endpoint cumple un propósito único y bien delimitado (ej. `validar_extension` solo verifica la integridad del formato de archivo; `process_image` orquesta la respuesta del controlador).
- **Manejo Defensivo de Excepciones:** Se implementaron validaciones con `ValueError` y códigos de estado HTTP controlados (400 Bad Request, 404 Not Found), evitando caídas inesperadas del servidor.

### 5.2 Configuración del Archivo `.coveragerc`
Se configuró el archivo `.coveragerc` en la raíz del proyecto para normar la medición:
```ini
[run]
source = src
omit = 
    tests/*
    venv/*
    .venv/*
    setup.py

[report]
show_missing = True
fail_under = 60

[html]
directory = htmlcov
```

---

## 6. MÉTRICAS DE VALIDACIÓN Y SUITE DE PRUEBAS

La verificación automática se realizó mediante la suite de pruebas unitarias (`unittest`) y el motor de cobertura (`coverage.py`):

```bash
# Comando de ejecucion de pruebas y cobertura
python -m coverage run -m unittest discover -s tests -v
python -m coverage report -m
```

### 6.1 Resultados Cuantitativos

| Módulo Evaluado | Sentencias (Stmts) | Líneas No Cubiertas (Miss) | Porcentaje de Cobertura | Estado |
| :--- | :---: | :---: | :---: | :---: |
| `src/validadores.py` | 18 | 0 | **100%** | Aprobado |
| `src/app.py` (Frontend Web) | 101 | 17 | **83%** | Aprobado |
| **TOTAL GLOBAL DEL PROYECTO** | **119** | **17** | **86%** | **EXCELENTE** |

- **Total de pruebas unitarias ejecutadas:** 18 tests (11 de validaciones + 7 de rutas y servicios frontend).
- **Tiempo total de ejecución de pruebas:** 0.857 segundos.
- **Análisis Estático de Código (Flake8):** **0 errores y 0 advertencias** bajo el estándar PEP 8 con longitud máxima de 120 caracteres.

---

## 7. AUTOMATIZACIÓN CI/CD CON GITHUB ACTIONS

Se integró un flujo de integración continua en `.github/workflows/ci.yml` que asegura que el repositorio nunca acepte código defectuoso:
1. Se dispara en cada `push` o `pull_request` a las ramas `main` y `develop`.
2. Instala dependencias en un entorno limpio Ubuntu Linux con Python 3.11.
3. Ejecuta `coverage run` y evalúa la regla `--fail-under=60`. Si la cobertura global cae por debajo del 60%, el pipeline bloquea automáticamente la entrega.

---

## 8. GUÍA DE SUSTENTACIÓN ANTE EL DOCENTE

### 8.1 Puntos Clave a Exponer en la Presentación
1. **Rol Personal:** Destacar que tu responsabilidad directa fue el **Desarrollo Frontend y la Arquitectura de Interfaz**, respetando la división del trabajo del equipo *Baje de C++*.
2. **Concepto de Cascarón Funcional:** Explicar que la interfaz ya es completamente interactiva y responde en milisegundos a la carga de fotos y descargas de planos CAD, facilitando una integración transparente con el backend.
3. **Evidencia de Calidad:** Enfatizar que el proyecto no solo tiene una interfaz moderna, sino que cuenta con un **86% de cobertura de código**, superando la meta de la Semana 11.

### 8.2 Respuestas Rápidas a Preguntas Típicas del Jurado

- **¿Por qué usar FastAPI en lugar de un Gradio estándar?**  
  *Respuesta:* "Gradio es excelente para prototipos rápidos de laboratorio, pero genera interfaces rígidas con aspecto de formulario escolar. Para Proteo AI necesitábamos una estación de trabajo técnica con vista dual comparativa, HUD de telemetría y tarjetas de descarga para AutoCAD. FastAPI nos permitió servir la interfaz de Google Stitch con Tailwind CSS y control total de la experiencia de usuario."

- **¿El archivo .DXF que descarga la página es real?**  
  *Respuesta:* "Sí. Está generado bajo el estándar AutoCAD R2010 mediante entidades `LWPOLYLINE` con coordenadas en milímetros, compatible para abrirse y modificarse directamente en AutoCAD, Civil3D o QCAD."

- **¿Cómo se comprobó que el código no tiene errores de estilo?**  
  *Respuesta:* "Corrimos `flake8 src/ tests/ --max-line-length=120`, obteniendo cero observaciones y cumplimiento total de PEP 8."

---

## 9. INSTRUCCIONES PARA EJECUCIÓN LOCAL

Para levantar y verificar la aplicación web localmente:

```powershell
# 1. Posicionarse en la carpeta del repositorio
cd "c:\Users\SAUL\Documents\Construccione de software\ia-proteo"

# 2. Iniciar el servidor web de desarrollo
python -m uvicorn src.app:app --reload --port 8000
```
Luego, abrir en el navegador: `http://localhost:8000`.

---
*Construcción de Software — Ciclo VII — Universidad Continental*
