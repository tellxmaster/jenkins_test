import unittest
from main import suma, resta, multiplicacion;

class TestFunciones(unittest.TestCase):
    
    def test_suma(self):
        self.assertEqual(suma(2, 3), 6)
        self.assertEqual(suma(-4, 9), 5)
        self.assertEqual(suma(0, 0), 0)

    def test_resta(self):
        self.assertEqual(resta(5, 2), 3)
        self.assertEqual(resta(0, 0), 0)
        self.assertEqual(resta(-5, -3), -2)

    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(2, 3), 6)
        self.assertEqual(multiplicacion(-4, 9), -36)
        self.assertEqual(multiplicacion(0, 0), 0)

if __name__ == '__main__':
    unittest.main()

