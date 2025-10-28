import unittest
from triangulo import classificar_triangulo

class TestTriangulo(unittest.TestCase):
    def test_equilatero(self):
        self.assertEqual(classificar_triangulo(3, 3, 3), "Equilátero")

    def test_isosceles(self):
        self.assertEqual(classificar_triangulo(3, 3, 2), "Isósceles")

    def test_escaleno(self):
        self.assertEqual(classificar_triangulo(3, 4, 5), "Escaleno")

    def test_invalido(self):
        self.assertEqual(classificar_triangulo(1, 2, 3), "Os lados não formam um triângulo.")

if __name__ == "__main__":
    unittest.main()
