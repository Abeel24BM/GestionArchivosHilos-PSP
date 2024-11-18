"""
Ejercicio: Crear una Clase de Hilo para Procesar Archivos
Objetivo: Crear una clase que herede de Thread para simular el procesamiento de archivos en paralelo.

Instrucciones:

Define una clase ProcesadorArchivo que herede de Thread.
En el método __init__, recibe un nombre de archivo y un número de líneas a procesar.
Sobrescribe el método run() para simular el procesamiento de cada línea del archivo, imprimiendo el nombre del archivo y el número de línea actual.
Crea una lista de nombres de archivos y genera un hilo ProcesadorArchivo para cada archivo en la lista.
Inicia todos los hilos y asegúrate de que el programa principal espere a que todos terminen antes de imprimir el mensaje "Todos los archivos han sido procesados".
Ejemplo de Salida Esperada:

Procesando archivo1.txt - Línea 1
Procesando archivo1.txt - Línea 2
Procesando archivo2.txt - Línea 1
Procesando archivo3.txt - Línea 1
Procesando archivo2.txt - Línea 2
Procesando archivo3.txt - Línea 2
...
Todos los archivos han sido procesados.
"""

import threading
import time

class ProcesadorArchivo(threading.Thread):
    def __init__(self, nombre, lineas):
        super().__init__()
        self.nombre = nombre
        self.lineas = lineas

    def run(self):
        for i, linea in enumerate(self.lineas, start=1):
            print(f"Procesando {self.nombre} - Línea {i}: {linea}")
            time.sleep(1)


# Archivos que posteriormente procesaremos
archivos = [
    {
        "nombre": "archivo1.txt",
        "contenidos": [
            "Linea 1",
            "Linea 2",
            "Linea 3"
        ]
    },
    {
        "nombre": "archivo2.txt",
        "contenidos": [
            "Linea 1",
            "Linea 2",
            "Linea 3"
        ]
    },
    {
        "nombre": "archivo3.txt",
        "contenidos": [
            "Linea 1",
            "Linea 2",
            "Linea 3"
        ]
    }
]

# Hilos
hilos = []
for archivo in archivos:
    hilo = ProcesadorArchivo(nombre=archivo["nombre"], lineas=archivo["contenidos"])
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

print("Todos los archivos han sido procesados.")


