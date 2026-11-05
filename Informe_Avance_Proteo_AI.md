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
- **Fecha de Actualización:** 5 de Noviembre de 2026
- **Repositorio Oficial:** [github.com/bajedec/Proteo-AI](https://github.com/bajedec/Proteo-AI)

---

## 1. RESUMEN EJECUTIVO

El presente informe detalla el progreso técnico consolidado en el desarrollo de **Proteo AI**, una plataforma orientada a ilustradores, modeladores 3D y diseñadores que automatiza la conversión de fotografías reales de objetos, estructuras y vehículos en **bocetos 2D (Line Art) y trazados vectoriales técnicos compatibles con AutoCAD (.DXF), Blender/Web (.SVG) e imágenes de alta definición (.PNG)**.

En estricto cumplimiento con la rúbrica oficial del curso (**Taller 3.4 — Avance Proyecto Final**), se ha consolidado el **Módulo Frontend**: una estación de trabajo CAD interactiva (*Aerospace Dark CAD Workstation*), desarrollada con **FastAPI, Tailwind CSS y JavaScript**, validada bajo la metodología **TDD (Test-Driven Development)** y alcanzando un **91% de cobertura de pruebas unitarias**, superando con honores el umbral exigido del 60% establecido en la **Semana 11** de la asignatura.

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

### 5.1 Ciclo TDD Evidenciado en Commits (Red - Green - Refactor)
En el repositorio se implementó y evidenció el ciclo completo de TDD para la nueva función `validar_tamano_archivo`:

1. **Fase RED (Fallo inicial):**
   - *Commit:* `1b4269b` — `test: [RED] ciclo TDD - agregar pruebas unitarias para validar_tamano_archivo`
   - *Acción:* Se escribieron las pruebas unitarias esperando rechazo de archivos mayores a 10 MB, archivos vacíos y tipos no numéricos. Las pruebas fallaron porque la función aún no existía en el código fuente.
2. **Fase GREEN (Paso a verde):**
   - *Commit:* `73aa1cc` — `feat: [GREEN] ciclo TDD - implementar validar_tamano_archivo para superar las pruebas`
   - *Acción:* Se implementó la lógica mínima necesaria en `src/validadores.py` para satisfacer las aserciones, logrando que todas las pruebas pasaran a verde.
3. **Fase REFACTOR (Optimización de código):**
   - *Commit:* `10db2ec` — `refactor: [REFACTOR] ciclo TDD - parametrizar validacion de tamano de archivo con subTest`
   - *Acción:* Se refactorizó la prueba unitaria utilizando `subTest` para evaluar múltiples rangos paramétricamente sin duplicar código.

### 5.2 Técnicas de Refactoring Aplicadas por el Equipo
- **Extract Constant:** Se erradicaron los números mágicos en `src/validadores.py` y `src/app.py`, centralizando constantes globales en mayúsculas (`LONGITUD_MINIMA_PROMPT = 3`, `LONGITUD_MAXIMA_PROMPT = 300`, `EXTENSIONES_PERMITIDAS = ('.png', '.jpg', '.jpeg')`, `TAMANO_MAXIMO_BYTES = 10 * 1024 * 1024`, `MAX_DIMENSION_PIXELS = 768`, `DEFAULT_RDP_TOLERANCE = 1.2`).
- **Single Responsibility Principle (SRP):** Cada función cumple una sola responsabilidad (validación de extensión, validación de tamaño, orquestación de respuesta).
- **Manejo Defensivo de Excepciones:** Se implementaron validaciones con `ValueError` y códigos HTTP controlados (400 Bad Request, 404 Not Found), evitando caídas inesperadas del servidor.

### 5.3 Configuración del Archivo `.coveragerc`
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

### 6.1 Resultados Cuantitativos Actualizados

| Módulo Evaluado | Sentencias (Stmts) | Líneas No Cubiertas (Miss) | Porcentaje de Cobertura | Estado |
| :--- | :---: | :---: | :---: | :---: |
| `src/validadores.py` | 27 | 0 | **100%** | Aprobado |
| `src/app.py` (Frontend Web) | 132 | 14 | **89%** | Aprobado |
| **TOTAL GLOBAL DEL PROYECTO** | **159** | **14** | **91%** | **EXCELENTE** |

- **Total de pruebas unitarias ejecutadas:** **24 tests** (17 de validaciones y TDD + 7 de rutas y servicios frontend).
- **Tiempo total de ejecución de pruebas:** 0.766 segundos.
- **Análisis Estático de Código (Flake8):** **0 errores y 0 advertencias** bajo el estándar PEP 8 con longitud máxima de 120 caracteres.

---

## 7. AUTOMATIZACIÓN CI/CD CON GITHUB ACTIONS

Se integró un flujo de integración continua en `.github/workflows/ci.yml` que asegura que el repositorio nunca acepte código defectuoso:
1. Se dispara en cada `push` o `pull_request` a las ramas `main` y `develop`.
2. Instala dependencias en un entorno limpio Ubuntu Linux con Python 3.11.
3. Ejecuta `coverage run` y evalúa la regla `--fail-under=60`. Si la cobertura global cae por debajo del 60%, el pipeline bloquea automáticamente la entrega.

---

## 8. CUMPLIMIENTO DE LA RÚBRICA OFICIAL DEL CURSO (20 / 20)

| Criterio de la Rúbrica | Requisito para Excelente (5 pts) | Estado en Proteo AI | Calificación |
| :--- | :--- | :--- | :---: |
| **S9: Tests Unitarios y Estructura** | Carpeta `tests/` con `test_*.py`, `unittest.TestCase`, todos los tests pasan y cubren casos límite. | 24 tests pasan en 0.76s; cubre casos de error, bordes y tipos. | **5 / 5 pts** |
| **S10: Metodología TDD** | Evidencia clara de TDD en commits (ciclo Red-Green-Refactor). | Commits explícitos `1b4269b` (RED), `73aa1cc` (GREEN), `10db2ec` (REFACTOR). | **5 / 5 pts** |
| **S11: Cobertura de Código** | `.coveragerc` configurado, cobertura $\ge 60\%$ y reporte HTML generado. | `.coveragerc` con fail_under=60; **91% de cobertura**; `htmlcov/` activo. | **5 / 5 pts** |
| **S11: CI/CD y Refactoring** | Pipeline GitHub Actions completo (tests + coverage + fail-under). Sin magic numbers. | Pipeline automatizado en `.github/workflows/ci.yml`; constantes globales. | **5 / 5 pts** |
| **TOTAL PROYECTADO** | | | **20 / 20 pts** |

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
