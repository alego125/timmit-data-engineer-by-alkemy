import os, sys
import unittest
from pathlib import Path
sys.path.append(os.path.join(Path(__file__).parent.parent, 'functions'))
import functions as f

# Imports para configurar docs_from_tests

from docs_from_tests.instrument_call_hierarchy import (
    instrument_and_import_package,
    initialise_call_hierarchy,
    finalise_call_hierarchy
)

instrument_and_import_package(os.path.join(Path(__file__)), 'functions')


class MyTest(unittest.TestCase):

    def test_hello_world(self):

        # Inicio de la secuencia, se comienza a grabar la gerarquia de llamadas
        initialise_call_hierarchy('start')

        # Palabra a testear
        to_check = "hola mundo"

        valid_word = f.get_valid_word()
        self.assertEqual(valid_word, to_check)

        # Finalizamos la secuencia
        root_call = finalise_call_hierarchy()

        # Retornamos el diagrama de secuencia
        sequence_diagram = root_call.sequence_diagram(
            show_private_functions=False,
            excluded_functions=[],
        )

        # Escribimos el archivo de la secuencia en formato markdown
        sequence_diagram_filename = os.path.join(os.path.dirname(__file__), '..', 'doc', 'diagramade secuencia.md')
        Path(sequence_diagram_filename).write_text(sequence_diagram)


if __name__ == '__main__':
    unittest.main()
