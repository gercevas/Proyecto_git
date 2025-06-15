# Proyecto de Temporizador, Cronómetro y Animación en Consola

Este proyecto implementa una librería Python organizada y reutilizable que ofrece tres funcionalidades principales:

1. Un temporizador con cuenta regresiva en segundos.
2. Un cronómetro con funciones de inicio y parada.
3. Un módulo de animación en consola como función adicional, que incluye impresión carácter por carácter y barra de carga.

## Repositorio

Repositorio público disponible en:  
[https://github.com/gercevas/Proyecto_git.git]

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/gercevas/Proyecto_git.git
cd Proyecto_git
```

2. Crea y activa un entorno virual

```bash
python3 -m venv venv
source venv/bin/activate  
```

3. Instala las dependencias

```bash
pip install -r requirements.txt
```

4. Instalación de la libreria principal

```bash
pip install -e .
```

## Estructura del proyecto

```
Proyecto_git/
├── scripts/
│   └── main.py
├── src/
│   ├── animacion/
│   │   ├── __init__.py
│   │   └── animacion.py
│   └── temporizador/
│       ├── __init__.py
│       ├── temporizador.py
│       └── cronometro.py
├── tests/
│   ├── test_animacion.py
│   ├── test_temporizador.py
│   └── test_cronometro.py
├── requirements.txt
├── setup.py
└── README.md
```

## Uso

Ejecuta el archivo main.py en el terminal para probar las tres funcionalidades:

```bash
python3 scripts/main.py
```

## Ejemplos de uso 

```bash
from temporizador.temporizador import Temporizador
from temporizador.cronometro import Cronometro
from animacion.animacion import Animacion

t = Temporizador(5)
t.iniciar()

c = Cronometro()
c.iniciar()
# tarea simulada
c.pausar()
print(f"Tiempo registrado: {c.obtener_tiempo()} segundos")

a = Animacion()
a.escribir_lento("Mensaje con animación.")
a.barra_de_carga(duracion=3)
```


## Ejecutar pruebas

### Por separado
```bash
python3 tests/test_temporizador.py
python3 tests/test_cronometro.py
python3 tests/test_animacion.py
```

### Todo el conjunto
```bash
pytest
``` 

## Requisitos

Python 3.7 o superior

## Autor

Germán Cevallos
https://github.com/gercevas

## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT.