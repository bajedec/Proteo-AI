"""
PROTEO AI - Servidor de Aplicacion y Controlador Frontend
Construccion de Software - Universidad Continental
Equipo: Baje de C++
Desarrollador Frontend: Saul Adain Huillca Rodriguez
"""

import os
import time
import uuid
from fastapi import FastAPI, File, Form, HTTPException, Request, UploadFile, status
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.validadores import validar_extension

# ---------------------------------------------------------------------------
# Constantes (Extract Constant: sin numeros magicos en el codigo)
# ---------------------------------------------------------------------------

# Rutas de directorios
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, "static")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
OUTPUTS_DIR = os.path.join(BASE_DIR, "outputs")

# Archivos subidos
BYTES_POR_MB = 1024 * 1024
MAX_UPLOAD_MB = 10
MAX_UPLOAD_BYTES = MAX_UPLOAD_MB * BYTES_POR_MB
JOB_ID_LENGTH = 8

# Parametros por defecto del formulario
DEFAULT_LINE_WEIGHT = 1.5
DEFAULT_RDP_TOLERANCE = 1.2

# Procesamiento de imagen (OpenCV)
MAX_DIMENSION = 768
SCALE_LIMIT = 1.0
BILATERAL_DIAMETER = 9
BILATERAL_SIGMA = 75
CANNY_LOW_THRESHOLD = 50
CANNY_HIGH_THRESHOLD = 150
MIN_CONTOUR_LENGTH = 5.0
MIN_POLYLINE_POINTS = 2
LATENCY_DECIMALS = 2

# Exportacion CAD (DXF)
DXF_VERSION = "R2010"
DXF_UNITS_MM = 4
DXF_LAYER_NAME = "PROTEO_TRAZOS"
DXF_LAYER_COLOR = 7

# Exportacion SVG
SVG_BACKGROUND_COLOR = "#061126"
SVG_STROKE_COLOR = "#38bdf8"

# Descargas
DEFAULT_MEDIA_TYPE = "application/octet-stream"
MEDIA_TYPES = {
    ".dxf": "application/dxf",
    ".svg": "image/svg+xml",
    ".png": "image/png",
}

# ---------------------------------------------------------------------------
# Inicializacion de la aplicacion
# ---------------------------------------------------------------------------
app = FastAPI(
    title="Proteo AI: Technical Sketch & CAD Studio",
    description="Frontend Web Application para generacion de bocetos 2D y exportacion CAD",
    version="1.0.0"
)

os.makedirs(OUTPUTS_DIR, exist_ok=True)
os.makedirs(STATIC_DIR, exist_ok=True)
os.makedirs(TEMPLATES_DIR, exist_ok=True)

# Montaje de archivos estaticos y templates
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
templates = Jinja2Templates(directory=TEMPLATES_DIR)


# ---------------------------------------------------------------------------
# Funciones auxiliares (Extract Method)
# ---------------------------------------------------------------------------

def validar_archivo_subido(nombre_archivo, contenido):
    """Valida extension, que no este vacio y que no supere el limite de tamano."""
    try:
        validar_extension(nombre_archivo)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    if len(contenido) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El archivo enviado esta vacio.",
        )

    if len(contenido) > MAX_UPLOAD_BYTES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El archivo supera el limite maximo de {MAX_UPLOAD_MB} MB.",
        )


def redimensionar_imagen(imagen):
    """Reduce la imagen para que su lado mayor no supere MAX_DIMENSION."""
    import cv2

    alto, ancho = imagen.shape[0], imagen.shape[1]
    escala = MAX_DIMENSION / max(alto, ancho)
    if escala < SCALE_LIMIT:
        nuevo_ancho, nuevo_alto = int(ancho * escala), int(alto * escala)
        reducida = cv2.resize(
            imagen, (nuevo_ancho, nuevo_alto), interpolation=cv2.INTER_AREA
        )
        return reducida, nuevo_ancho, nuevo_alto
    return imagen, ancho, alto


def extraer_bordes(imagen):
    """Convierte a grises, suaviza y detecta bordes con Canny."""
    import cv2

    grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    suavizada = cv2.bilateralFilter(
        grises, BILATERAL_DIAMETER, BILATERAL_SIGMA, BILATERAL_SIGMA
    )
    return cv2.Canny(suavizada, CANNY_LOW_THRESHOLD, CANNY_HIGH_THRESHOLD)


def generar_dxf(bordes, alto, tolerancia_rdp, ruta_dxf):
    """Vectoriza los bordes, guarda el DXF y devuelve (num_polilineas, poligonos_svg)."""
    import cv2
    import ezdxf

    doc = ezdxf.new(DXF_VERSION)
    doc.header['$INSUNITS'] = DXF_UNITS_MM
    msp = doc.modelspace()
    doc.layers.add(name=DXF_LAYER_NAME, color=DXF_LAYER_COLOR)

    contornos, _ = cv2.findContours(bordes, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    total_polilineas = 0
    poligonos_svg = []

    for contorno in contornos:
        if cv2.arcLength(contorno, True) < MIN_CONTOUR_LENGTH:
            continue
        aproximado = cv2.approxPolyDP(contorno, epsilon=tolerancia_rdp, closed=True)
        if len(aproximado) >= MIN_POLYLINE_POINTS:
            puntos_cad = [
                (float(pt[0][0]), float(alto - pt[0][1])) for pt in aproximado
            ]
            msp.add_lwpolyline(
                puntos_cad, close=True, dxfattribs={"layer": DXF_LAYER_NAME}
            )
            total_polilineas += 1
            puntos_svg = " ".join([f"{pt[0][0]},{pt[0][1]}" for pt in aproximado])
            poligonos_svg.append(f'    <polygon points="{puntos_svg}" />')

    doc.saveas(ruta_dxf)
    return total_polilineas, poligonos_svg


def generar_svg(poligonos, ancho, alto, grosor_linea, ruta_svg):
    """Escribe el archivo SVG con los poligonos vectorizados."""
    encabezado = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{ancho}" height="{alto}" '
        f'viewBox="0 0 {ancho} {alto}">'
    )
    cuerpo = "\n".join(poligonos)
    contenido = f"""{encabezado}
  <rect width="100%" height="100%" fill="{SVG_BACKGROUND_COLOR}"/>
  <g stroke="{SVG_STROKE_COLOR}" stroke-width="{grosor_linea}" fill="none"
     stroke-linecap="round" stroke-linejoin="round">
{cuerpo}
  </g>
</svg>"""
    with open(ruta_svg, "w", encoding="utf-8") as f:
        f.write(contenido)


def obtener_media_type(nombre_archivo):
    """Devuelve el tipo MIME segun la extension del archivo."""
    extension = os.path.splitext(nombre_archivo)[1].lower()
    return MEDIA_TYPES.get(extension, DEFAULT_MEDIA_TYPE)


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Renderiza la estacion de trabajo principal del Frontend."""
    return templates.TemplateResponse(request=request, name="index.html")


@app.get("/health")
async def health_check():
    """Endpoint de estado para verificacion de disponibilidad y metadatos del Frontend."""
    return {
        "status": "ok",
        "app": "Proteo AI CAD Studio",
        "team": "Baje de C++",
        "module": "Frontend",
        "developer": "Saul Adain Huillca Rodriguez",
        "active_theme": "Aerospace Dark CAD"
    }


@app.post("/api/process")
async def process_image(
    file: UploadFile = File(...),
    preset: str = Form("blueprint"),
    line_weight: float = Form(DEFAULT_LINE_WEIGHT),
    rdp_tolerance: float = Form(DEFAULT_RDP_TOLERANCE),
    isolate_bg: bool = Form(True)
):
    """
    Recibe la imagen desde el Frontend, valida extension y tamano,
    y ejecuta la generacion del boceto y vectores CAD.
    """
    # 1. Validacion con logica de negocio (src.validadores)
    contents = await file.read()
    validar_archivo_subido(file.filename, contents)

    job_id = uuid.uuid4().hex[:JOB_ID_LENGTH]
    ext = os.path.splitext(file.filename)[1].lower()
    input_path = os.path.join(OUTPUTS_DIR, f"input_{job_id}{ext}")
    png_path = os.path.join(OUTPUTS_DIR, f"boceto_{job_id}.png")
    dxf_path = os.path.join(OUTPUTS_DIR, f"plano_{job_id}.dxf")
    svg_path = os.path.join(OUTPUTS_DIR, f"vector_{job_id}.svg")

    with open(input_path, "wb") as f:
        f.write(contents)

    # 2. Medicion de tiempo de procesamiento
    t_start = time.perf_counter()

    # Procesamiento inteligente con OpenCV / DXF (siempre disponible sin colapsar la app)
    import cv2

    img = cv2.imread(input_path)
    if img is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se pudo decodificar la imagen enviada.",
        )

    img_resized, new_w, new_h = redimensionar_imagen(img)
    edges = extraer_bordes(img_resized)

    # Boceto blanco y negro limpio
    cv2.imwrite(png_path, cv2.bitwise_not(edges))

    # Plano DXF y vector SVG
    polylines_count, svg_polygons = generar_dxf(edges, new_h, rdp_tolerance, dxf_path)
    generar_svg(svg_polygons, new_w, new_h, line_weight, svg_path)

    t_latency = round(time.perf_counter() - t_start, LATENCY_DECIMALS)

    return JSONResponse({
        "success": True,
        "latency": t_latency,
        "polylines": polylines_count,
        "sketch_url": f"/api/download/boceto_{job_id}.png",
        "dxf_url": f"/api/download/plano_{job_id}.dxf",
        "svg_url": f"/api/download/vector_{job_id}.svg",
        "png_url": f"/api/download/boceto_{job_id}.png"
    })


@app.get("/api/download/{filename}")
async def download_file(filename: str):
    """Permite al usuario descargar los archivos generados en formatos DXF, SVG y PNG."""
    safe_filename = os.path.basename(filename)
    file_path = os.path.join(OUTPUTS_DIR, safe_filename)

    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El archivo solicitado no existe.",
        )

    return FileResponse(
        file_path,
        media_type=obtener_media_type(safe_filename),
        filename=safe_filename,
    )
