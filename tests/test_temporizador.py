import unittest
import time
from temporizador.temporizador import Temporizador

class TestTemporizador(unittest.TestCase):
    """Pruebas para la clase Temporizador."""

    def test_atributo_segundos(self):
        """Debe almacenar correctamente el valor inicial de segundos."""
        t = Temporizador(10)
        self.assertEqual(t.segundos, 10)

    def test_cuenta_regresiva(self):
        """La cuenta regresiva debe mostrar el mensaje final correctamente."""
        # Evitar pausas reales con monkeypatch manual
        original_sleep = time.sleep
        time.sleep = lambda x: None

        t = Temporizador(3)

        # Captura de salida por consola
        from io import StringIO
        import sys
        salida = StringIO()
        sys_stdout_original = sys.stdout
        sys.stdout = salida

        t.iniciar()

        # Restaurar sys.stdout y time.sleep
        sys.stdout = sys_stdout_original
        time.sleep = original_sleep

        self.assertIn("¡Tiempo terminado!", salida.getvalue())


if __name__ == '__main__':
    unittest.main()
    print("All tests passed!")
