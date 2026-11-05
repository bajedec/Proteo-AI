# Reglas de Proyecto y Estándares Documentales - Proteo AI

Este archivo define las directrices obligatorias para el desarrollo y generación de entregables en el proyecto **Proteo AI** de la Universidad Continental.

## 1. Identidad y Ámbito del Proyecto
- **Estudiante / Desarrollador:** Saul Adain Huillca Rodriguez (`74401464@continental.edu.pe`)
- **Rol en el Equipo (*Baje de C++*):** Frontend Developer
- **Institución:** Universidad Continental - Facultad de Ingeniería - Ingeniería de Sistemas e Informática
- **Curso:** Construcción de Software (Docente: Ing. Henderson Nozart Gibaja Reyes)

## 2. Estándares de Código y Calidad (Rúbrica Continental)
- **Cobertura de Pruebas:** Mantener siempre $\ge 60\%$ de cobertura de pruebas unitarias (estándar actual: >90%).
- **Linter:** 0 errores de `flake8` (`flake8 src/ tests/ --max-line-length=120`).
- **TDD:** Commits organizados siguiendo el ciclo Red-Green-Refactor.
- **Desacoplamiento:** El Frontend (`src/app.py`, `templates/`, `static/`) debe permanecer desacoplado y funcional independientemente de los pesos pesados del modelo de IA (`model.onnx`).

## 3. Estándares de Documentación e Informes (FastDoc)
- **Velocidad de Generación:** Para informes oficiales con tablas y capturas de pantalla, utilizar el motor rápido `continental-fast-reports` (`python-docx`).
- **Tablas:** Formato con cabecera corporativa `#0F172A`, filas alternas sombreadas y texto centrado.
- **Imágenes:** Incrustación directa desde rutas locales del disco con formato APA 7 (Título superior en cursiva, imagen a 6 pulgadas, nota explicativa inferior).
- **Regla Zero-LaTeX:** Prohibido el uso de sintaxis LaTeX (`$...$`) en documentos de Word o Google Docs. Utilizar siempre tipografía Unicode directa (`≥`, `≤`, `ε`, `²`, `×`, `→`).
- **Sincronización:** Documentos de Google Docs deben estar vinculados a la cuenta institucional `74401464@continental.edu.pe`.
