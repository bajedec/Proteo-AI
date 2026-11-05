
"""
Pruebas Unitarias para el Módulo Frontend (FastAPI & Google Stitch UI)
Semana 11 - Construcción de Software (Universidad Continental)
Desarrollador Frontend: Saul Adain Huillca Rodriguez
"""

import io
import unittest

from fastapi.testclient import TestClient
from PIL import Image

from src.app import app


class TestFrontendApp(unittest.TestCase):
    """Suite de pruebas unitarias para el controlador y endpoints del Frontend."""

    @classmethod
    def setUpClass(cls):
        """Inicializa el cliente de pruebas."""
        cls.client = TestClient(app)

    def _crear_imagen_dummy(self, width=100, height=100, color="red"):
        """Genera una imagen PNG en memoria para las pruebas."""
        buffer = io.BytesIO()
        imagen = Image.new("RGB", (width, height), color=color)
        imagen.save(buffer, format="PNG")
        buffer.seek(0)
        return buffer

    def test_home_page_renders_successfully(self):
        """Verifica que la página principal cargue correctamente."""
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn("PROTEO", response.text)
        self.assertIn("CAD-STUDIO", response.text)
        self.assertIn("Saul Huillca", response.text)

    def test_health_check_endpoint(self):
        """Verifica el estado del servicio y la información del módulo."""
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["module"], "Frontend")
        self.assertEqual(
            data["developer"],
            "Saul Adain Huillca Rodriguez"
        )

    def test_process_invalid_file_extension(self):
        """Verifica que los archivos con extensiones no permitidas sean rechazados."""
        pdf_content = b"%PDF-1.4 dummy pdf content"

        files = {
            "file": (
                "documento.pdf",
                pdf_content,
                "application/pdf"
            )
        }

        response = self.client.post("/api/process", files=files)

        self.assertEqual(response.status_code, 400)
        self.assertIn(
            "Extension de archivo no permitida",
            response.json()["detail"]
        )

    def test_process_empty_file(self):
        """Verifica que un archivo vacío sea rechazado."""
        files = {
            "file": (
                "vacio.png",
                b"",
                "image/png"
            )
        }

        response = self.client.post("/api/process", files=files)

        self.assertEqual(response.status_code, 400)
        self.assertIn(
            "vacio",
            response.json()["detail"].lower()
        )

    def test_process_valid_image(self):
        """Verifica el procesamiento correcto de una imagen válida."""
        img_bytes = self._crear_imagen_dummy(
            width=120,
            height=120,
            color="blue"
        )

        files = {
            "file": (
                "test_auto.png",
                img_bytes,
                "image/png"
            )
        }

        data = {
            "preset": "blueprint",
            "line_weight": "1.5",
            "rdp_tolerance": "1.2",
            "isolate_bg": "true"
        }

        response = self.client.post(
            "/api/process",
            files=files,
            data=data
        )

        self.assertEqual(response.status_code, 200)

        res_data = response.json()

        self.assertTrue(res_data["success"])
        self.assertIn("dxf_url", res_data)
        self.assertIn("svg_url", res_data)
        self.assertIn("png_url", res_data)

        self.assertGreaterEqual(
            res_data["latency"],
            0.0
        )

    def test_download_nonexistent_file(self):
        """Verifica que un archivo inexistente devuelva error 404."""
        response = self.client.get(
            "/api/download/archivo_fantasma_12345.dxf"
        )

        self.assertEqual(response.status_code, 404)

    def test_download_valid_generated_file(self):
        """Verifica que un archivo generado pueda descargarse correctamente."""

        # 1. Generar imagen de prueba
        img_bytes = self._crear_imagen_dummy()

        files = {
            "file": (
                "descarga_test.png",
                img_bytes,
                "image/png"
            )
        }

        # 2. Procesar imagen
        response = self.client.post(
            "/api/process",
            files=files
        )

        self.assertEqual(response.status_code, 200)

        dxf_url = response.json()["dxf_url"]

        # 3. Descargar archivo generado
        download_response = self.client.get(dxf_url)

        self.assertEqual(download_response.status_code, 200)

        self.assertGreater(
            len(download_response.content),
            0
        )


if __name__ == "__main__":
    unittest.main( )
