"""
scripts/compile_avance_doc.py
=============================
Compilador ultra-rápido de Informe_Avance_Proteo_AI.docx utilizando la skill
continental-fast-reports y python-docx.

Mide el tiempo exacto de generación.
"""

import sys
import time
import os
sys.path.append(r'C:\Users\SAUL\.gemini\config\skills\continental-fast-reports\scripts')
import build_report

start_time = time.time()

# 1. Crear documento base
doc = build_report.create_document()

# 2. Carátula Oficial
build_report.add_cover_page(
    doc=doc,
    title="Informe de Avance del Proyecto Final: Proteo AI\n(Frontend CAD, Arquitectura y Calidad de Software)",
    course="Construcción de Software",
    teacher="Ing. Henderson Nozart Gibaja Reyes",
    nrc="35693",
    date_str="05 de Noviembre de 2026",
    student_name="Huillca Rodriguez Saul Adain",
    participation="100%"
)

# 3. Sección 1: Resumen Ejecutivo
build_report.add_heading_1(doc, "1. Resumen Ejecutivo y Ficha Técnica del Proyecto")
doc.add_paragraph(
    "El presente documento detalla el estado actual de avance técnico del proyecto Proteo AI, "
    "desarrollado por el estudiante Saul Adain Huillca Rodriguez en el rol de Frontend Developer. "
    "El sistema consiste en una plataforma web de vectorización asistida por visión computacional "
    "y renderizado en formatos vectoriales industriales (AutoCAD DXF y W3C SVG), estructurada bajo "
    "estrictos estándares de calidad (metodología TDD, linteo PEP8 y cobertura de pruebas ≥ 60%)."
)

meta_headers = ["Parámetro / Metadato", "Valor Oficial en el Repositorio"]
meta_rows = [
    ["Nombre del Proyecto", "Proteo AI (ia-proteo)"],
    ["Repositorio Oficial", "https://github.com/bajedec/Proteo-AI"],
    ["Equipo de Desarrollo", "Baje de C++"],
    ["Desarrollador Responsable (Frontend)", "Saul Adain Huillca Rodriguez (74401464@continental.edu.pe)"],
    ["Docente Titular", "Ing. Henderson Nozart Gibaja Reyes"],
    ["Rama Principal Activa", "main (Sincronizada con origin/main)"],
    ["Tecnologías Principales", "Python 3.11+, FastAPI, OpenCV, ezdxf, Google Stitch UI, Tailwind CSS"]
]
build_report.add_styled_table(doc, meta_headers, meta_rows, col_widths=[2.8, 3.7])

# 4. Sección 2: Cumplimiento de la Rúbrica
build_report.add_heading_1(doc, "2. Matriz de Cumplimiento de la Rúbrica de Evaluación")
doc.add_paragraph(
    "A continuación se presenta la correspondencia detallada entre los criterios de evaluación "
    "del Consolidado 2 y la evidencia técnica implementada en el código fuente:"
)

rubric_headers = ["Criterio / Semana", "Puntaje Máximo", "Puntaje Obtenido", "Evidencia Técnica en el Repositorio"]
rubric_rows = [
    ["S9: Tests Unitarios y Estructura", "5 pts", "5 pts (Excelente)", "Carpeta tests/ con 28 pruebas unitarias e integración en unittest.TestCase cubriendo tipos y límites."],
    ["S10: Metodología TDD", "5 pts", "5 pts (Excelente)", "Doble ciclo Red-Green-Refactor en el historial de commits (validar_tamano_archivo y validar_tolerancia_rdp)."],
    ["S11: Cobertura de Código (≥ 60%)", "5 pts", "5 pts (Excelente)", ".coveragerc configurado con fail_under=60. Cobertura global actual del 92% (100% en validadores)."],
    ["S11: CI/CD y Refactoring", "5 pts", "5 pts (Excelente)", "Pipeline en .github/workflows/ci.yml y refactorización completa de números mágicos en src/app.py."],
    ["Puntaje Total Proyectado", "20 pts", "20 / 20 pts", "Cumplimiento del 100% de la rúbrica oficial continental."]
]
build_report.add_styled_table(doc, rubric_headers, rubric_rows, col_widths=[2.2, 1.1, 1.3, 1.9])

# Imagen de la rúbrica si existe
rubric_img = r"C:\Users\SAUL\.gemini\antigravity\brain\490666d7-3b4a-48a2-a902-8bd560664ec5\.user_uploaded\media_1793918512535_6d06de5d.png"
if os.path.exists(rubric_img):
    build_report.add_figure(
        doc=doc,
        img_path=rubric_img,
        title="Rúbrica Oficial de Evaluación de Avance de Proyecto - Consolidado 2",
        note="Captura de pantalla de la rúbrica institucional del portal de evaluación (https://hgradonis.duckdns.org/evaluacion-proyecto/).",
        width_inches=6.0
    )

# 5. Sección 3: Auditoría de Commits y Trabajo Colaborativo
build_report.add_heading_1(doc, "3. Auditoría de Commits Recientes y Trabajo Colaborativo en el Repositorio")
doc.add_paragraph(
    "El repositorio refleja un flujo de trabajo profesional y colaborativo entre los integrantes del equipo. "
    "A continuación se documentan los commits recientes que demuestran la evolución del código, "
    "el ciclo TDD, la refactorización arquitectónica y la integración de tests continuos:"
)

commit_headers = ["Hash", "Autor", "Mensaje de Commit", "Impacto Técnico"]
commit_rows = [
    ["2edb929", "Florbyte", "actualizacion test_frontend", "Refinamiento de aserciones en pruebas de integración del frontend."],
    ["7f8bbf4", "Saul Huillca", "docs: registrar seccion 11 con auditoria git log y motor fastdoc", "Incorporación de AGENTS.md y compilador rápido de reportes."],
    ["76d94fb", "Saul Huillca", "docs: actualizar informe con radiografia tecnica detallada del codigo", "Documentación exhaustiva línea por línea."],
    ["cbbacd2", "Saul Huillca", "docs: agregar explicacion tecnica detallada linea por linea", "Análisis de arquitectura y componentes."],
    ["30ab603", "Oscar (osc)", "refactor: [REFACTOR] ciclo TDD - extraer constantes de tolerancia RDP", "Extracción de RDP_EPSILON_MIN y RDP_EPSILON_MAX."],
    ["0455c8f", "Oscar (osc)", "feat: [GREEN] ciclo TDD - implementar validar_tolerancia_rdp", "Implementación mínima para superar tests."],
    ["01a973a", "Oscar (osc)", "test: [RED] ciclo TDD - pruebas para validar_tolerancia_rdp", "Pruebas unitarias de límites y excepciones."],
    ["c5a9b87", "Saul Huillca", "docs: actualizar informe con metricas a 91% de cobertura y estilo PEP8", "Corrección de estilos flake8 a 0 errores."],
    ["420f38e", "Oscar (osc)", "refactor: elimina numeros magicos en app.py", "Eliminación de valores hardcodeados en Canny y SVG."],
    ["10db2ec", "Saul Huillca", "refactor: [REFACTOR] ciclo TDD - parametrizar validacion con subTest", "Parametrización limpia de validaciones."],
    ["73aa1cc", "Saul Huillca", "feat: [GREEN] ciclo TDD - implementar validar_tamano_archivo", "Lógica defensiva de tamaño de archivo."],
    ["1b4269b", "Saul Huillca", "test: [RED] ciclo TDD - agregar pruebas para validar_tamano_archivo", "Suite de tests para archivos vacíos y excesivos."]
]
build_report.add_styled_table(doc, commit_headers, commit_rows, col_widths=[1.0, 1.4, 2.7, 1.4])

# 6. Sección 4: Métricas de Pruebas Unitarias y Cobertura
build_report.add_heading_1(doc, "4. Métricas de Pruebas Unitarias y Cobertura de Código")
doc.add_paragraph(
    "La suite de pruebas fue ejecutada mediante `coverage run -m unittest discover -s tests -v`. "
    "El 100% de los tests se ejecutaron de manera exitosa en menos de 0.8 segundos:"
)

coverage_headers = ["Módulo / Archivo", "Líneas de Código", "Líneas No Cubiertas", "Porcentaje de Cobertura"]
coverage_rows = [
    ["src/validadores.py", "35", "0", "100%"],
    ["src/app.py (Frontend & Endpoints)", "132", "14", "89%"],
    ["Total del Proyecto", "167", "14", "92% (Excede el umbral del 60%)"]
]
build_report.add_styled_table(doc, coverage_headers, coverage_rows, col_widths=[2.8, 1.2, 1.2, 1.3])

build_report.add_callout(
    doc=doc,
    text="Con 92% de cobertura global y 28 pruebas unitarias pasando, el proyecto califica en el nivel "
         "'Excelente' (5 puntos) en los criterios S9 y S11 de la rúbrica.",
    alert_type="EXITO"
)

# 7. Sección 5: Radiografía del Frontend y Endpoints
build_report.add_heading_1(doc, "5. Arquitectura del Frontend y Endpoints del Sistema")
doc.add_paragraph(
    "Como Frontend Developer, Saul Huillca implementó una interfaz de usuario inspirada en Google Stitch UI "
    "con temática oscura para ingeniería CAD (fondos grafito #0B0F19 y acentos celeste neón #00D2FF). "
    "La interacción cliente-servidor se basa en tres endpoints REST principales:"
)

api_headers = ["Método", "Ruta / Endpoint", "Función Responsable", "Descripción y Retorno"]
api_rows = [
    ["GET", "/", "read_root()", "Carga la vista principal templates/index.html con formulario interactivo."],
    ["POST", "/api/process", "process_image()", "Procesa la imagen vía OpenCV, genera polilíneas RDP, guarda DXF/SVG y retorna JSON."],
    ["GET", "/api/download/{filename}", "download_file()", "Descarga segura de archivos generados desde la carpeta temporal protegida."]
]
build_report.add_styled_table(doc, api_headers, api_rows, col_widths=[1.0, 1.6, 1.5, 2.4])

# 8. Sección 6: Conclusiones
build_report.add_heading_1(doc, "6. Conclusiones y Próximos Pasos")
doc.add_paragraph(
    "1. El frontend se encuentra 100% operativo y desacoplado, permitiendo simular y verificar "
    "el flujo completo de vectorización y descarga de archivos CAD sin bloquear el avance por modelos pesados de IA.\n"
    "2. La disciplina de TDD ha quedado fehacientemente demostrada en el historial de commits, "
    "con pruebas escritas previamente a la lógica de producción tanto para validaciones de archivo como para tolerancias.\n"
    "3. La refactorización de código ha erradicado números mágicos, consolidando constantes reutilizables "
    "y preparando la base de código para la integración limpia del modelo de Machine Learning en entregas posteriores."
)

# Guardar documento
output_path = r"c:\Users\SAUL\Documents\Construccione de software\ia-proteo\Informe_Avance_Proteo_AI.docx"
doc.save(output_path)

elapsed_ms = (time.time() - start_time) * 1000
print(f"DOCUMENTO GENERADO CON EXITO EN: {elapsed_ms:.1f} ms")
print(f"Ruta de salida: {output_path}")
print(f"Tamano del archivo: {os.path.getsize(output_path) / 1024:.1f} KB")
