"""
Módulo que implementa un cronómetro con funciones de inicio, pausa y reinicio.
"""

import time

class Cronometro:
    """
    Clase que representa un cronómetro con funciones básicas.
    """

    def __init__(self):
        """
        Inicializa el cronómetro.
        """
        self._inicio = None
        self._en_marcha = False
        self._tiempo_total = 0.0

    def iniciar(self):
        """
        Inicia el cronómetro (o lo reanuda si estaba en pausa).
        """
        if not self._en_marcha:
            self._inicio = time.time()
            self._en_marcha = True
            print("Cronómetro iniciado.")

    def pausar(self):
        """
        Pausa el cronómetro y acumula el tiempo transcurrido.
        """
        if self._en_marcha:
            tiempo_actual = time.time() - self._inicio
            self._tiempo_total += tiempo_actual
            self._en_marcha = False
            print(f"Cronómetro pausado en {self._tiempo_total:.2f} segundos.")

    def reiniciar(self):
        """
        Reinicia el cronómetro a 0.
        """
        self._inicio = None
        self._tiempo_total = 0.0
        self._en_marcha = False
        print("Cronómetro reiniciado.")

    def obtener_tiempo(self) -> float:
        """
        Devuelve el tiempo total transcurrido en segundos.

        Returns:
            float: Tiempo en segundos.
        """
        if self._en_marcha:
            tiempo_actual = time.time() - self._inicio
            return self._tiempo_total + tiempo_actual
        return self._tiempo_total
