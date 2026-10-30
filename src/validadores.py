"""Validaciones basicas para Proteo-AI."""

LONGITUD_MINIMA_PROMPT = 3
LONGITUD_MAXIMA_PROMPT = 300
EXTENSIONES_PERMITIDAS = (".png", ".jpg", ".jpeg")


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
        raise ValueError("El nombre del archivo debe ser texto")
        
    if not nombre_archivo.lower().endswith(EXTENSIONES_PERMITIDAS):
        raise ValueError("Extension de archivo no permitida")
        
    return nombre_archivo


