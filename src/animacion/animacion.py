"""
Módulo que contiene animaciones simples para consola.
"""

import time
import sys


class Animacion:
    """
    Clase que implementa animaciones básicas para la consola.
    """

    def __init__(self, velocidad: float = 0.05):
        """
        Inicializa la animación con una velocidad de animación.

        Args:
            velocidad (float): Tiempo de espera entre caracteres o pasos (en segundos).
        """
        self.velocidad = velocidad

    def escribir_lento(self, texto: str):
        """
        Muestra el texto carácter por carácter con efecto de máquina de escribir.

        Args:
            texto (str): Texto a mostrar lentamente.
        """
        for letra in texto:
            print(letra, end='', flush=True)
            time.sleep(self.velocidad)
        print()  # nueva línea al final

    def barra_de_carga(self, duracion: float = 3.0):
        """
        Muestra una barra de carga en consola.

        Args:
            duracion (float): Duración total de la barra de carga (en segundos).
        """
        pasos = 20
        intervalo = duracion / pasos
        for i in range(pasos + 1):
            barra = '█' * i + '-' * (pasos - i)
            porcentaje = int((i / pasos) * 100)
            sys.stdout.write(f'\rCargando: [{barra}] {porcentaje}%')
            sys.stdout.flush()
            time.sleep(intervalo)
        print("\n¡Carga completa!")
