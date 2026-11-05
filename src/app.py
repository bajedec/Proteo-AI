"""
PROTEO AI - Servidor de Aplicacion y Controlador Frontend
Construccion de Software - Universidad Continental
Equipo: Baje de C++
Desarrollador Frontend: Saul Adain Huillca Rodriguez
"""

import os
import time
import uuid
from fastapi import FastAPI, File, Form, HTTPException, Request, UploadFile
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.validadores import validar_extension

# Inicializacion de la aplicacion
app = FastAPI(
    title="Proteo AI: Technical Sketch & CAD Studio",
    description="Frontend Web Application para generacion de bocetos 2D y exportacion CAD",
    version="1.0.0"
)

# Rutas de directorios
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, "static")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
OUTPUTS_DIR = os.path.join(BASE_DIR, "outputs")

os.makedirs(OUTPUTS_DIR, exist_ok=True)
os.makedirs(STATIC_DIR, exist_ok=True)
os.makedirs(TEMPLATES_DIR, exist_ok=True)

# Montaje de archivos estaticos y templates
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
templates = Jinja2Templates(directory=TEMPLATES_DIR)


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
    line_weight: float = Form(1.5),
    rdp_tolerance: float = Form(1.2),
    isolate_bg: bool = Form(True)
):
    """
    Recibe la imagen desde el Frontend, valida extension y tamano,
    y ejecuta la generacion del boceto y vectores CAD.
    """
    # 1. Validacion con logica de negocio (src.validadores)
    try:
        validar_extension(file.filename)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    contents = await file.read()
    if len(contents) == 0:
        raise HTTPException(status_code=400, detail="El archivo enviado esta vacio.")

    # Limite maximo de 10 MB
    if len(contents) > 10 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="El archivo supera el limite maximo de 10 MB.")

    job_id = str(uuid.uuid4())[:8]
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
    import ezdxf

    img = cv2.imread(input_path)
    if img is None:
        raise HTTPException(status_code=400, detail="No se pudo decodificar la imagen enviada.")

    h, w = img.shape[:2]
    max_dim = 768
    scale = max_dim / max(h, w)
    if scale < 1.0:
        new_w, new_h = int(w * scale), int(h * scale)
        img_resized = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_AREA)
    else:
        img_resized = img
        new_w, new_h = w, h

    # Extraccion de lineas estructurales
    gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
    blurred = cv2.bilateralFilter(gray, 9, 75, 75)
    edges = cv2.Canny(blurred, 50, 150)

    # Generar boceto blanco y negro limpio
    sketch = cv2.bitwise_not(edges)
    cv2.imwrite(png_path, sketch)

    # Generacion de plano AutoCAD DXF R2010
    doc = ezdxf.new("R2010")
    doc.header['$INSUNITS'] = 4  # mm
    msp = doc.modelspace()
    doc.layers.add(name="PROTEO_TRAZOS", color=7)

    contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    polylines_count = 0
    svg_polygons = []

    for cnt in contours:
        if cv2.arcLength(cnt, True) < 5.0:
            continue
        approx = cv2.approxPolyDP(cnt, epsilon=rdp_tolerance, closed=True)
        if len(approx) >= 2:
            pts_cad = [(float(pt[0][0]), float(new_h - pt[0][1])) for pt in approx]
            msp.add_lwpolyline(pts_cad, close=True, dxfattribs={"layer": "PROTEO_TRAZOS"})
            polylines_count += 1
            pts_svg = " ".join([f"{pt[0][0]},{pt[0][1]}" for pt in approx])
            svg_polygons.append(f'    <polygon points="{pts_svg}" />')

    doc.saveas(dxf_path)

    # Generacion de SVG
    svg_header = f'<svg xmlns="http://www.w3.org/2000/svg" width="{new_w}" height="{new_h}" ' \
                 f'viewBox="0 0 {new_w} {new_h}">'
    svg_body = "\n".join(svg_polygons)
    svg_content = f"""{svg_header}
  <rect width="100%" height="100%" fill="#061126"/>
  <g stroke="#38bdf8" stroke-width="{line_weight}" fill="none" stroke-linecap="round" stroke-linejoin="round">
{svg_body}
  </g>
</svg>"""
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)

    t_latency = round(time.perf_counter() - t_start, 2)

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
        raise HTTPException(status_code=404, detail="El archivo solicitado no existe.")

    media_type = "application/octet-stream"
    if safe_filename.endswith(".dxf"):
        media_type = "application/dxf"
    elif safe_filename.endswith(".svg"):
        media_type = "image/svg+xml"
    elif safe_filename.endswith(".png"):
        media_type = "image/png"

    return FileResponse(file_path, media_type=media_type, filename=safe_filename)
