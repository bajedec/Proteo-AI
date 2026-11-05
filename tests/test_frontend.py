"""
Pruebas Unitarias para el Modulo Frontend (FastAPI & Google Stitch UI)
Semana 11 - Construccion de Software (Universidad Continental)
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
        cls.client = TestClient(app)

    def _crear_imagen_dummy(self, width=100, height=100, color="red"):
        """Genera una imagen en memoria para pruebas de subida sin depender del disco."""
        buf = io.BytesIO()
        img = Image.new("RGB", (width, height), color=color)
        img.save(buf, format="PNG")
        buf.seek(0)
        return buf

    def test_home_page_renders_successfully(self):
        """Verifica que la pagina principal cargue con status 200 y contenga los componentes del Frontend."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("PROTEO", response.text)
        self.assertIn("CAD-STUDIO", response.text)
        self.assertIn("Saul Huillca", response.text)

    def test_health_check_endpoint(self):
        """Verifica que el endpoint de salud devuelva la informacion de rol y estado."""
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["module"], "Frontend")
        self.assertEqual(data["developer"], "Saul Adain Huillca Rodriguez")

    def test_process_invalid_file_extension(self):
        """Verifica que un archivo con extension no permitida sea rechazado con status 400."""
        pdf_content = b"%PDF-1.4 dummy pdf content"
        files = {"file": ("documento.pdf", pdf_content, "application/pdf")}
        response = self.client.post("/api/process", files=files)
        self.assertEqual(response.status_code, 400)
        self.assertIn("Extension de archivo no permitida", response.json()["detail"])

    def test_process_empty_file(self):
        """Verifica que un archivo de 0 bytes sea rechazado con status 400."""
        files = {"file": ("vacio.png", b"", "image/png")}
        response = self.client.post("/api/process", files=files)
        self.assertEqual(response.status_code, 400)
        self.assertIn("vacio", response.json()["detail"].lower())

    def test_process_valid_image(self):
        """Verifica que una imagen valida procese correctamente y genere los enlaces de descarga."""
        img_bytes = self._crear_imagen_dummy(width=120, height=120, color="blue")
        files = {"file": ("test_auto.png", img_bytes, "image/png")}
        data = {
            "preset": "blueprint",
            "line_weight": "1.5",
            "rdp_tolerance": "1.2",
            "isolate_bg": "true"
        }
        response = self.client.post("/api/process", files=files, data=data)
        self.assertEqual(response.status_code, 200)
        res_data = response.json()
        self.assertTrue(res_data["success"])
        self.assertIn("dxf_url", res_data)
        self.assertIn("svg_url", res_data)
        self.assertIn("png_url", res_data)
        self.assertGreaterEqual(res_data["latency"], 0.0)

    def test_download_nonexistent_file(self):
        """Verifica que solicitar un archivo inexistente devuelva error 404."""
        response = self.client.get("/api/download/archivo_fantasma_12345.dxf")
        self.assertEqual(response.status_code, 404)

    def test_download_valid_generated_file(self):
        """Verifica que un archivo generado se pueda descargar correctamente."""
        # 1. Procesar imagen
        img_bytes = self._crear_imagen_dummy()
        files = {"file": ("descarga_test.jpg", img_bytes, "image/jpeg")}
        res = self.client.post("/api/process", files=files)
        self.assertEqual(res.status_code, 200)
        dxf_url = res.json()["dxf_url"]

        # 2. Descargar archivo
        download_res = self.client.get(dxf_url)
        self.assertEqual(download_res.status_code, 200)
        self.assertGreater(len(download_res.content), 0)


if __name__ == "__main__":
    unittest.main()
