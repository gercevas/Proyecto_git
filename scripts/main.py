import time

# Importar las clases de cada módulo
from temporizador.temporizador import Temporizador
from temporizador.cronometro import Cronometro
from animacion.animacion import Animacion

print("\n=== ANIMACIÓN DE BIENVENIDA ===")
anim = Animacion(velocidad=0.1)
anim.escribir_lento("¡Bienvenido a la demostración de la librería, espero que se haya instalado sin problema!")
anim.barra_de_carga(duracion=3)

print("\n=== PRUEBA DEL TEMPORIZADOR ===")
t = Temporizador(5)  # 5 segundos
t.iniciar()

print("\n=== PRUEBA DEL CRONÓMETRO ===")
c = Cronometro()
c.iniciar()
time.sleep(3.2)  # simula una tarea de 3.2 segundos
c.pausar()
print(f"Tiempo registrado: {c.obtener_tiempo():.2f} segundos")

print("\n=== FIN DE LA DEMOSTRACIÓN ===")
anim.escribir_lento("Gracias por usar esta libreria, espero que te haya sido útil :)")