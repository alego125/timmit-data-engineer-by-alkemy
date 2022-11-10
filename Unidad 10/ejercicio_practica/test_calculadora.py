"""Module that test Class Calculadora functionalities
"""
import unittest
from calculadora import Calculadora


class TestCalculadoraOperations(unittest.TestCase):

    calculadora = Calculadora()

    # Test addition by asserEqual and assertTrue in possitives and negatives values and then
    def test_addition(self):
        """Addition method test which is done in 2 ways, with assertEqual, assertTrue
        """

        self.assertEqual(self.calculadora.add(2, 2), 4, "Incorrect expected value")
        self.assertEqual(self.calculadora.add(-4, 2), -2, "Incorrect expected value")
        self.assertTrue(self.calculadora.add(2.2, 3.2) == 5.4, f"Return {self.calculadora.add(2.2, 3.2)} and should have been returned {5.4}")

    # Test subtraction by asserEqual and assertTrue in possitives and negatives values and then
    def test_subtraction(self):
        """Subtraction method test which is done in 2 ways, with assertEqual, assertTrue
        """

        self.assertEqual(self.calculadora.subtract(8, 4), 4, "Incorrect expected value")
        self.assertEqual(self.calculadora.subtract(4, 8), -4, "Incorrect expected value")
        self.assertEqual(self.calculadora.subtract(8, 8), 0, "Incorrect expected value")
        self.assertTrue(self.calculadora.subtract(3.2, 2.2) == 1, f"Return {self.calculadora.subtract(3.2, 2.2)} and should have been returned {1}")

    # Test multiplication by asserEqual and assertTrue in possitives and negatives values and then
    def test_multiplication(self):
        """Multiplication method test which is done in 2 ways, with assertEqual, assertTrue
        """

        self.assertEqual(self.calculadora.multiply(2, 2), 4, "Incorrect expected value")
        self.assertEqual(self.calculadora.multiply(-2, 2), -4, "Incorrect expected value")
        self.assertTrue(self.calculadora.multiply(2.5, 3) == 7.5, f"Return {self.calculadora.multiply(2.5, 3)} and should have been returned {7.5}")

    # Test division by asserEqual and assertTrue in possitives and negatives values and then
    def test_division(self):
        """Division method test which is done in 2 ways, with assertEqual, assertTrue
        """

        self.assertEqual(self.calculadora.divide(8, 2), 4, "Incorrect expected value")
        self.assertTrue(self.calculadora.divide(2.2, 2) == 1.1, f"Return {self.calculadora.divide(2.2, 2)} and should have been returned {1.1}")

        with self.assertRaises(ZeroDivisionError, msg="ZeroDivisionError not work"):
            self.calculadora.divide(2, 0)


if __name__ == '__main__':
    unittest.main()
