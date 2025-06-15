"""
Módulo que implementa un temporizador con cuenta regresiva en segundos.
"""

import time

class Temporizador:
    """
    Clase que representa un temporizador de cuenta regresiva.
    """

    def __init__(self, segundos: int):
        """
        Inicializa el temporizador con los segundos deseados.

        Args:
            segundos (int): Tiempo en segundos para la cuenta atrás.
        """
        self.segundos = segundos

    def iniciar(self):
        """
        Inicia la cuenta regresiva desde el número de segundos especificado.
        """
        print(f"Iniciando temporizador de {self.segundos} segundos...")
        for i in range(self.segundos, 0, -1):
            print(f"Tiempo restante: {i} segundos", end='\r')  # Bonus animación con \r
            time.sleep(1)
        print("\n¡Tiempo terminado!")
