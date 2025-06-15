"""
Pruebas unitarias para el módulo de animación.
"""

import unittest
import time
from io import StringIO
import sys
from animacion.animacion import Animacion


class TestAnimacion(unittest.TestCase):
    """Pruebas para la clase Animacion."""

    def setUp(self):
        self.anim = Animacion(velocidad=0.01)

    def test_escribir_lento(self):
        """Verifica que escribir_lento imprima correctamente el texto."""
        texto = "Hola mundo"
        salida = StringIO()
        sys_stdout_original = sys.stdout
        sys.stdout = salida

        # Evita sleep real
        original_sleep = time.sleep
        time.sleep = lambda _: None

        self.anim.escribir_lento(texto)

        sys.stdout = sys_stdout_original
        time.sleep = original_sleep

        self.assertIn(texto, salida.getvalue())

    def test_barra_de_carga(self):
        """Verifica que la barra de carga finalice correctamente."""
        salida = StringIO()
        sys_stdout_original = sys.stdout
        sys.stdout = salida

        original_sleep = time.sleep
        time.sleep = lambda _: None

        self.anim.barra_de_carga(duracion=1.0)

        sys.stdout = sys_stdout_original
        time.sleep = original_sleep

        self.assertIn("¡Carga completa!", salida.getvalue())


if __name__ == '__main__':
    unittest.main()
    print("All tests passed!")
