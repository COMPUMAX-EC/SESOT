# Sistema Experto para Mantenimiento de CPU e Impresoras

Este proyecto implementa un sistema experto para proporcionar soluciones de mantenimiento de CPU e impresoras. Está diseñado para ejecutarse en un Raspberry Pi 3 e incluye:

- **Base de conocimientos**: Contiene hechos y reglas sobre mantenimiento.
- **Motor de inferencia**: Deduce soluciones basadas en hechos y reglas.
- **Soporte en línea**: Permite interacción en lenguaje natural.
- **Interfaz gráfica**: Proporciona una interfaz amigable para los usuarios.

## Estructura del Proyecto

- `base_conocimientos/`: Contiene la base de conocimientos.
- `motor_inferencia/`: Implementación del motor de inferencia.
- `soporte_linea/`: Módulo para interacción en lenguaje natural.
- `interfaz_grafica/`: Archivos relacionados con la interfaz gráfica.

## Requisitos

- Python 3.7 o superior
- Librerías: `flask`, `nltk`, `tkinter`

## Instalación

1. Clonar el repositorio.
2. Instalar las dependencias con `pip install -r requirements.txt`.
3. Ejecutar el sistema con `python main.py`.

## Uso

El sistema permite a los usuarios ingresar problemas relacionados con CPU e impresoras y proporciona soluciones basadas en la base de conocimientos.