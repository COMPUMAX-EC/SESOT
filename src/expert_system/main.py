#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema Experto para Mantenimiento de CPU e Impresoras
Optimizado para Raspberry Pi 3

Este es el archivo principal para ejecutar el sistema experto.
Puede ejecutarse en modo consola o con interfaz gráfica.

Uso:
    python main.py          # Ejecuta con interfaz gráfica
    python main.py --cli    # Ejecuta en modo consola
"""

import sys
import os

# Agregar la carpeta del proyecto al PYTHONPATH
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from base_conocimientos import obtener_accion, reglas
from procesador_lenguaje import procesar_entrada


def ejecutar_modo_consola():
    """Ejecuta el sistema experto en modo consola."""
    print("=" * 60)
    print("  SISTEMA EXPERTO - MANTENIMIENTO DE CPU E IMPRESORAS")
    print("  Optimizado para Raspberry Pi 3")
    print("  Modo: Consola")
    print("=" * 60)
    print("\nEscriba su problema en lenguaje natural.")
    print("Ejemplos:")
    print("  - 'Mi computadora no enciende'")
    print("  - 'La impresora tiene papel atascado'")
    print("  - 'El CPU está muy lento'")
    print("  - 'Mi impresora no imprime'")
    print("\nEscriba 'salir' para terminar.\n")
    
    while True:
        try:
            entrada = input(">>> Describa su problema: ")
        except (KeyboardInterrupt, EOFError):
            print("\n\n¡Gracias por usar el Sistema Experto! ¡Adiós!")
            break
            
        if entrada.lower() == "salir":
            print("\n¡Gracias por usar el Sistema Experto! ¡Adiós!")
            break
        if not entrada.strip():
            print("Por favor, ingrese una descripción del problema.\n")
            continue
        
        print("\n" + "-" * 50)
        palabras_clave = procesar_entrada(entrada)
        print(f"[INFO] Palabras clave detectadas: {palabras_clave}")
        solucion = obtener_accion(palabras_clave)
        print(solucion)
        print("-" * 50 + "\n")


def ejecutar_modo_gui():
    """Ejecuta el sistema experto con interfaz gráfica."""
    try:
        from interfaz import SistemaExpertoGUI
        import tkinter as tk
        
        root = tk.Tk()
        app = SistemaExpertoGUI(root)
        root.mainloop()
    except ImportError as e:
        print(f"Error al importar la interfaz gráfica: {e}")
        print("Ejecutando en modo consola...")
        ejecutar_modo_consola()
    except Exception as e:
        print(f"Error al iniciar la interfaz gráfica: {e}")
        print("Ejecutando en modo consola...")
        ejecutar_modo_consola()


def mostrar_ayuda():
    """Muestra la ayuda del sistema."""
    print("""
Sistema Experto para Mantenimiento de CPU e Impresoras
======================================================

Uso:
    python main.py [opciones]

Opciones:
    --cli       Ejecutar en modo consola (sin interfaz gráfica)
    --gui       Ejecutar con interfaz gráfica (por defecto)
    --help, -h  Mostrar esta ayuda

Descripción:
    Este sistema experto proporciona soluciones para problemas
    comunes de mantenimiento de CPU e impresoras. Está optimizado
    para ejecutarse en Raspberry Pi 3.

Ejemplos de consultas:
    - "Mi computadora no enciende"
    - "La impresora tiene papel atascado"
    - "El CPU está muy lento"
    - "Mi impresora no imprime"
    - "La computadora se sobrecalienta"
    """)


if __name__ == "__main__":
    # Procesar argumentos de línea de comandos
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg in ['--help', '-h']:
            mostrar_ayuda()
        elif arg == '--cli':
            ejecutar_modo_consola()
        elif arg == '--gui':
            ejecutar_modo_gui()
        else:
            print(f"Opción no reconocida: {arg}")
            mostrar_ayuda()
    else:
        # Por defecto, ejecutar con interfaz gráfica
        ejecutar_modo_gui()
