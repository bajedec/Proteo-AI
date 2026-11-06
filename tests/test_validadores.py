import unittest

from src.validadores import (
    validar_extension,
    validar_prompt,
    validar_tamano_archivo,
    validar_tolerancia_rdp,
)


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

    def test_espacios_no_cuentan_para_el_largo(self):
        """El largo se mide despues de quitar espacios sobrantes."""
        with self.assertRaisesRegex(ValueError, "demasiado corto"):
            validar_prompt("  ab  ")


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

    def test_extension_no_texto(self):
        with self.assertRaises(ValueError):
            validar_extension(12345)


class TestValidarTamanoArchivo(unittest.TestCase):
    """Pruebas de validar_tamano_archivo: peso maximo permitido 10 MB."""

    def test_tamano_valido(self):
        """Un archivo de 500 KB debe ser aceptado."""
        self.assertEqual(validar_tamano_archivo(1024 * 500), 1024 * 500)

    def test_tamano_limite_exacto(self):
        """El limite exacto de 10 MB es aceptado."""
        limite = 10 * 1024 * 1024
        self.assertEqual(validar_tamano_archivo(limite), limite)

    def test_tamano_excede_limite(self):
        """Un archivo mayor a 10 MB debe lanzar ValueError."""
        limite_excedido = (10 * 1024 * 1024) + 1
        with self.assertRaises(ValueError):
            validar_tamano_archivo(limite_excedido)

    def test_tamano_cero_o_negativo(self):
        """Un archivo vacio o con tamano negativo debe lanzar ValueError."""
        with self.assertRaises(ValueError):
            validar_tamano_archivo(0)
        with self.assertRaises(ValueError):
            validar_tamano_archivo(-100)

    def test_tamano_no_numerico(self):
        """Tipos de datos invalidos deben lanzar ValueError."""
        with self.assertRaises(ValueError):
            validar_tamano_archivo("10MB")
        with self.assertRaises(ValueError):
            validar_tamano_archivo(None)
        with self.assertRaises(ValueError):
            validar_tamano_archivo(True)

    def test_varios_tamanos_con_subtest(self):
        """Refactor: prueba parametrizada con subTest para validar multiples rangos."""
        casos = [
            (1024, True),
            (5 * 1024 * 1024, True),
            (10 * 1024 * 1024, True),
            (0, False),
            (-50, False),
            (11 * 1024 * 1024, False),
        ]
        for tamano, esperado_valido in casos:
            with self.subTest(tamano=tamano):
                if esperado_valido:
                    self.assertEqual(validar_tamano_archivo(tamano), tamano)
                else:
                    with self.assertRaises(ValueError):
                        validar_tamano_archivo(tamano)


class TestValidarToleranciaRdp(unittest.TestCase):
    """Ciclo TDD: la tolerancia RDP debe ser numerica y estar en rango."""

    def test_tolerancia_valida(self):
        self.assertEqual(validar_tolerancia_rdp(1.2), 1.2)

    def test_limites_exactos(self):
        self.assertEqual(validar_tolerancia_rdp(0.1), 0.1)
        self.assertEqual(validar_tolerancia_rdp(10), 10)

    def test_tolerancia_no_numerica(self):
        for valor in ("1.2", None, True):
            with self.assertRaises(ValueError):
                validar_tolerancia_rdp(valor)

    def test_tolerancia_fuera_de_rango(self):
        for valor in (0, 0.05, 50, -1):
            with self.assertRaises(ValueError):
                validar_tolerancia_rdp(valor)


if __name__ == "__main__":
    unittest.main()
