"""Validaciones basicas para Proteo-AI."""

LONGITUD_MINIMA_PROMPT = 3
LONGITUD_MAXIMA_PROMPT = 300
EXTENSIONES_PERMITIDAS = (".png", ".jpg", ".jpeg")
TAMANO_MAXIMO_BYTES = 10 * 1024 * 1024  # 10 MB maximo para imagenes CAD


def validar_prompt(prompt):
    """Devuelve el prompt sin espacios sobrantes o lanza ValueError."""
    if not isinstance(prompt, str):
        raise ValueError("El prompt debe ser texto")
    prompt_limpio = prompt.strip()
    if len(prompt_limpio) < LONGITUD_MINIMA_PROMPT:
        raise ValueError("El prompt es demasiado corto")
    if len(prompt_limpio) > LONGITUD_MAXIMA_PROMPT:
        raise ValueError("El prompt es demasiado largo")
    return prompt_limpio


def validar_extension(nombre_archivo):
    """Verifica que el archivo sea una imagen permitida."""
    if not isinstance(nombre_archivo, str):
        raise ValueError("El nombre de archivo debe ser texto")
    if not nombre_archivo.lower().endswith(EXTENSIONES_PERMITIDAS):
        raise ValueError("Extension de archivo no permitida")
    return nombre_archivo


def validar_tamano_archivo(tamano_bytes):
    """Verifica que el peso del archivo en bytes no exceda el limite permitido."""
    if not isinstance(tamano_bytes, (int, float)) or isinstance(tamano_bytes, bool):
        raise ValueError("El tamano del archivo debe ser un numero")
    if tamano_bytes <= 0:
        raise ValueError("El tamano del archivo debe ser mayor a 0 bytes")
    if tamano_bytes > TAMANO_MAXIMO_BYTES:
        raise ValueError("El archivo excede el tamano maximo permitido (10 MB)")
    return tamano_bytes
