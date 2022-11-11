"""Module that test Class Calculadora functionalities
"""
import unittest
import sys
import os
import datetime
# Move path to root path and then import module calculadora
sys.path.append('C:/Users/ale/Desktop/Programa Data Engeniere/Unidad 11/ejercicio_practico')
import functions.calculadora as calc

from pathlib import Path
# Imports to docs_from_tests config
from docs_from_tests.instrument_call_hierarchy import(
    instrument_and_import_package,
    initialise_call_hierarchy,
    finalise_call_hierarchy
)

# return path to this file test
sys.path.append('')
instrument_and_import_package(os.path.join(Path(__file__).parent.absolute(), '..', 'functions'), 'functions')


class TestCalculadoraOperations(unittest.TestCase):

    calculadora = calc.Calculadora()

    # Test addition by asserEqual and assertTrue in possitives and negatives values and then
    def test_addition(self):
        """Addition method test which is done in 2 ways, with assertEqual and assertTrue
        """
        initialise_call_hierarchy('start')

        self.assertEqual(self.calculadora.add(2, 2), 4, "Incorrect expected value")
        self.assertEqual(self.calculadora.add(-4, 2), -2, "Incorrect expected value")
        self.assertTrue(self.calculadora.add(2.2, 3.2) == 5.4, f"Return {self.calculadora.add(2.2, 3.2)} and should have been returned {5.4}")

        with self.assertRaises(TypeError, msg="TypeError not work"):
            self.calculadora.add(2, 's')

        # Create root call finalise the event and build the diagram, finish save it into file
        root_call = finalise_call_hierarchy()

        sequence_diagram = root_call.sequence_diagram(
            show_private_functions=False,
            excluded_functions=[]
        )

        sequence_diagram_filename = os.path.join(os.path.dirname(__file__), '..', 'doc', 'diagrama_de_secuencia_addition_function.md')
        Path(sequence_diagram_filename).write_text(sequence_diagram)

    # Test subtraction by asserEqual and assertTrue in possitives and negatives values and then
    def test_subtraction(self):
        """Subtraction method test which is done in 2 ways, with assertEqual and assertTrue
        """
        initialise_call_hierarchy('start')

        self.assertEqual(self.calculadora.subtract(8, 4), 4, "Incorrect expected value")
        self.assertEqual(self.calculadora.subtract(4, 8), -4, "Incorrect expected value")
        self.assertEqual(self.calculadora.subtract(8, 8), 0, "Incorrect expected value")
        self.assertTrue(self.calculadora.subtract(3.2, 2.2) == 1, f"Return {self.calculadora.subtract(3.2, 2.2)} and should have been returned {1}")

        with self.assertRaises(TypeError, msg="TypeError not work"):
            self.calculadora.subtract(2, 's')

        root_call = finalise_call_hierarchy()
        sequence_diagram = root_call.sequence_diagram(
            show_private_functions=False,
            excluded_functions=[]
        )

        sequence_diagram_filename = os.path.join(os.path.dirname(__file__), '..', 'doc', 'diagrama_de_secuencia_subtraction_function.md')
        Path(sequence_diagram_filename).write_text(sequence_diagram)

    # Test multiplication by asserEqual and assertTrue in possitives and negatives values and then
    def test_multiplication(self):
        """Multiplication method test which is done in 2 ways, with assertEqual and assertTrue
        """
        initialise_call_hierarchy('start')

        self.assertEqual(self.calculadora.multiply(2, 2), 4, "Incorrect expected value")
        self.assertEqual(self.calculadora.multiply(-2, 2), -4, "Incorrect expected value")
        self.assertTrue(self.calculadora.multiply(2.5, 3) == 7.5, f"Return {self.calculadora.multiply(2.5, 3)} and should have been returned {7.5}")

        with self.assertRaises(TypeError, msg="TypeError not work"):
            self.calculadora.multiply("s", "s")

        root_call = finalise_call_hierarchy()
        sequence_diagram = root_call.sequence_diagram(
            show_private_functions=False,
            excluded_functions=[]
        )

        sequence_diagram_filename = os.path.join(os.path.dirname(__file__), '..', 'doc', 'diagrama_de_secuencia_multiplication_function.md')
        Path(sequence_diagram_filename).write_text(sequence_diagram)

    # Test division by asserEqual and assertTrue in possitives and negatives values and then get riased errors
    def test_division(self):
        """Division method test which is done in 2 ways, with assertEqual and assertTrue
        """
        initialise_call_hierarchy('start')

        self.assertEqual(self.calculadora.divide(8, 2), 4, "Incorrect expected value")
        self.assertTrue(self.calculadora.divide(2.2, 2) == 1.1, f"Return {self.calculadora.divide(2.2, 2)} and should have been returned {1.1}")

        with self.assertRaises(ZeroDivisionError, msg="ZeroDivisionError not work"):
            self.calculadora.divide(2, 0)

        with self.assertRaises(TypeError, msg="TypeError not work"):
            self.calculadora.divide(2, 's')

        root_call = finalise_call_hierarchy()
        sequence_diagram = root_call.sequence_diagram(
            show_private_functions=False,
            excluded_functions=[]
        )

        sequence_diagram_filename = os.path.join(os.path.dirname(__file__), '..', 'doc', 'diagrama_de_secuencia_division_function.md')
        Path(sequence_diagram_filename).write_text(sequence_diagram)

    def test_all(self):
        """Test that contain the logic of other tests to create an a unic graph with all conections
        """
        initialise_call_hierarchy('start')

        self.assertEqual(self.calculadora.add(2, 2), 4, "Incorrect expected value")
        self.assertEqual(self.calculadora.add(-4, 2), -2, "Incorrect expected value")
        self.assertTrue(self.calculadora.add(2.2, 3.2) == 5.4, f"Return {self.calculadora.add(2.2, 3.2)} and should have been returned {5.4}")

        self.assertEqual(self.calculadora.subtract(8, 4), 4, "Incorrect expected value")
        self.assertEqual(self.calculadora.subtract(4, 8), -4, "Incorrect expected value")
        self.assertEqual(self.calculadora.subtract(8, 8), 0, "Incorrect expected value")
        self.assertTrue(self.calculadora.subtract(3.2, 2.2) == 1, f"Return {self.calculadora.subtract(3.2, 2.2)} and should have been returned {1}")

        self.assertEqual(self.calculadora.multiply(2, 2), 4, "Incorrect expected value")
        self.assertEqual(self.calculadora.multiply(-2, 2), -4, "Incorrect expected value")
        self.assertTrue(self.calculadora.multiply(2.5, 3) == 7.5, f"Return {self.calculadora.multiply(2.5, 3)} and should have been returned {7.5}")
        with self.assertRaises(TypeError, msg="TypeError not work"):
            self.calculadora.multiply("Hola", 's')

        self.assertEqual(self.calculadora.divide(8, 2), 4, "Incorrect expected value")
        self.assertTrue(self.calculadora.divide(2.2, 2) == 1.1, f"Return {self.calculadora.divide(2.2, 2)} and should have been returned {1.1}")
        with self.assertRaises(ZeroDivisionError, msg="ZeroDivisionError not work"):
            self.calculadora.divide(2, 0)

        with self.assertRaises(TypeError, msg="TypeError not work"):
            self.calculadora.divide(2, 's')

        root_call = finalise_call_hierarchy()
        sequence_diagram = root_call.sequence_diagram(
            show_private_functions=False,
            excluded_functions=[]
        )

        sequence_diagram_filename = os.path.join(os.path.dirname(__file__), '..', 'doc', 'diagrama_de_secuencia_all_function.md')
        Path(sequence_diagram_filename).write_text(sequence_diagram)


def header(file):
    file.write('\n')
    file.write('******************TESTING**************************')
    file.write('\n')
    file.write('\n')
    now = datetime.datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    file.write("Date -> " + date_time)
    file.write('\n')
    file.write('\n')
    file.write('***************************************************')
    file.write('\n')
    return file


# En que cambia que sea stderr, stdin, stdout en out
def main(out=sys.stderr, verbosity=3):
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out, verbosity=verbosity).run(suite)


if __name__ == '__main__':
    with open('../doc/testing.txt', 'w') as file:
        file = header(file)
        main(file)
    unittest.main()
