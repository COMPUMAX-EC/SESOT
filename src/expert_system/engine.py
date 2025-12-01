# Motor de Inferencia
# Este archivo contiene el motor de inferencia para el sistema experto.
# Optimizado para Raspberry Pi 

import sys
import os

# Agregar la carpeta raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(_file_), "..")))

from base_conocimientos.base_conocimientos import obtener_accion
from soporte_linea.procesador_lenguaje import procesar_entrada

# Función para procesar entradas en lenguaje natural
def procesar_entrada_usuario(entrada):
    """
    Procesa la entrada del usuario y busca una solución.
    1. Extrae palabras clave de la entrada
    2. Busca coincidencias en la base de conocimientos
    3. Retorna la solución encontrada
    """
    palabras_clave = procesar_entrada(entrada)
    print(f"[DEBUG] Palabras clave detectadas: {palabras_clave}")
    solucion = obtener_accion(palabras_clave)
    return solucion

# Ejemplo de uso del motor de inferencia
if _name_ == "_main_":
    print("=" * 60)
    print("  SISTEMA EXPERTO - MANTENIMIENTO DE CPU E IMPRESORAS")
    print("  Optimizado para Raspberry Pi 3")
    print("=" * 60)
    print("\nEscriba su problema en lenguaje natural.")
    print("Ejemplos:")
    print("  - 'Mi computadora no enciende'")
    print("  - 'La impresora tiene papel atascado'")
    print("  - 'El CPU está muy lento'")
    print("  - 'Mi impresora no imprime'")
    print("\nEscriba 'salir' para terminar.\n")
    
    while True:
        entrada = input(">>> Describa su problema: ")
        if entrada.lower() == "salir":
            print("\n¡Gracias por usar el Sistema Experto! ¡Adiós!")
            break
        if not entrada.strip():
            print("Por favor, ingrese una descripción del problema.\n")
            continue
        
        print("\n" + "-" * 50)
        solucion = procesar_entrada_usuario(entrada)
        print(solucion)
        print("-" * 50 + "\n")