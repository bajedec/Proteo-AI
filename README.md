==================================================
PLAN: PROTEO
==================================================

# Proteo

## Equipo: Baje de C++
- Diego Isaias Gutierrez Ruiz — DevOps / CI-CD
- Saul Adain Huilca Rodriguez — Desarrollador Frontend
- Oscar Josue Pastor Quispe — Desarrollador Fullstack
- Flor Camila Huallpa Cobos — QA / Testing
- Humbero Zamora Moscoso — Desarrollador Backend

## Problema
lo artistas de videojuegos indie y creadores de contenido que necesitan bocetos 2D como base para dibujar personajes u objetos. 

## Solucion
para este proyecto se usa un modelo de IA de detecciones de bordes y visión por computadora a partir de una foto subida por el usuario y generar automáticamente un boceto 2D el mine art de lo que detecta.

## Modelo de IA
- **Categoria:** image-classification
- **Modelo:** [stable-diffusion-v1-5/stable-diffusion-v-1-5](https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5)
- **Input:** imagen jpg/png
- **Output:** Un papa de los bordes en 2D 
- **Justificacion:** este modelo se eligio por que se aprovecha la arquitectura Vision Transformer, la cual captura relaciones globales en la imagen.

## Dataset
- **Nombre:** proteo-sketch-dataset
- **Registros:** 1000
- **Columnas:** Describe las columnas de tu dataset: 
-photo: imagen original en formato RGB
-sketch: imagen en escala de grises generada automaticamente con dteccion de bordes
-file_name: nombre del archivo que vincula cada par toto-boceto

## Stack
- **Lenguaje:** python
- **Framework:** gradio
- **ML:** Hugging Face Transformers
- **Testing:** unittest + TDD
- **CI/CD:** GitHub Actions

## Instalacion
```bash
git clone https://github.com/bajedec/Proteo-AI
cd proteo
python -m venv venv
venv\\Scripts\\activate
pip install -r requirements.txt
```

## Tests
```bash
python -m unittest discover -s tests -v
```

---
*Proyecto Final — Construccion de Software — Universidad Continental*

--- ESTRUCTURA ---
proteo/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── preprocess.py
│   ├── model.py
│   ├── postprocess.py
├── tests/
│   ├── __init__.py
│   ├── test_preprocess.py
│   ├── test_model.py
├── training/
│   ├── train.py
│   ├── evaluate.py
│   └── config.json
├── data/
│   ├── raw/
│   └── processed/
├── models/  (no subir a git)
├── static/
├── templates/
└── docs/


--- CI/CD ---
name: CI - Proteo

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.10", "3.11"]

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v5
      with:
        python-version: ${{ matrix.python-version }}

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run tests
      run: |
        python -m unittest discover -s tests -v

    - name: Lint
      run: |
        pip install flake8
        flake8 src/ --max-line-length=120

--- REQUIREMENTS ---
transformers>=4.35.0
datasets>=2.14.0
pandas>=2.0.0
numpy>=1.24.0
Pillow>=10.0.0
matplotlib>=3.7.0
accelerate
