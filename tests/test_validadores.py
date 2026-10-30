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


if __name__ == "__main__":
    unittest.main()
