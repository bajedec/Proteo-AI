import unittest

from src.validadores import validar_extension, validar_prompt


class TestValidarPrompt(unittest.TestCase):
    def test_prompt_valido(self):
        self.assertEqual(validar_prompt("  un paisaje  "), "un paisaje")

    def test_prompt_no_texto(self):
        with self.assertRaises(ValueError):
            validar_prompt(123)

    def test_prompt_muy_corto(self):
        with self.assertRaises(ValueError):
            validar_prompt("a")

    def test_prompt_muy_largo(self):
        with self.assertRaises(ValueError):
            validar_prompt("x" * 1000)


class TestValidarExtension(unittest.TestCase):
    def test_extension_valida(self):
        self.assertEqual(validar_extension("foto.PNG"), "foto.PNG")

    def test_extension_invalida(self):
        with self.assertRaises(ValueError):
            validar_extension("documento.pdf")
class TestValidarExtension(unittest.TestCase):
    """Pruebas de validar_extension: solo se permiten .png, .jpg y .jpeg."""

    def test_extension_valida(self):
        """Una extension permitida (aunque este en mayusculas) se acepta."""
        self.assertEqual(validar_extension("foto.PNG"), "foto.PNG")

    def test_extension_jpeg_valida(self):
        """Tambien se aceptan .jpg y .jpeg."""
        self.assertEqual(validar_extension("foto.jpg"), "foto.jpg")
        self.assertEqual(validar_extension("foto.jpeg"), "foto.jpeg")

    def test_extension_invalida(self):
        """Un PDF no es una imagen: debe lanzar ValueError."""
        with self.assertRaises(ValueError):
            validar_extension("documento.pdf")

    def test_extension_txt_rechazada(self):
        """Un archivo de texto tambien debe ser rechazado."""
        with self.assertRaises(ValueError):
            validar_extension("notas.txt")

    def test_sin_extension_rechazada(self):
        """Un nombre sin extension no es una imagen valida."""
        with self.assertRaises(ValueError):
            validar_extension("archivo")

    def test_doble_extension_rechazada(self):
        """Gana la ultima extension: foto.png.exe no es una imagen."""
        with self.assertRaises(ValueError):
            validar_extension("foto.png.exe")


if __name__ == "__main__":
    unittest.main()
