# Procesador de Lenguaje Natural
# Este módulo se encarga de tokenizar, normalizar y extraer palabras clave de las entradas del usuario.
# Optimizado para Raspberry Pi 3 - Sin dependencias pesadas de NLTK

import re

# Lista de palabras vacías en español (stopwords)
PALABRAS_VACIAS = {
    'el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas',
    'de', 'del', 'al', 'a', 'en', 'con', 'por', 'para',
    'que', 'es', 'son', 'está', 'están', 'este', 'esta',
    'mi', 'tu', 'su', 'mis', 'tus', 'sus', 'me', 'te', 'se',
    'y', 'o', 'pero', 'si', 'no', 'como', 'muy', 'más',
    'ya', 'hay', 'tiene', 'tienen', 'puede', 'pueden',
    'ser', 'estar', 'hacer', 'tener', 'poder',
    'le', 'lo', 'les', 'nos', 'yo', 'él', 'ella', 'ellos',
    'cuando', 'donde', 'quien', 'cual', 'cuales',
    'todo', 'todos', 'toda', 'todas', 'otro', 'otra',
    'ese', 'esa', 'esos', 'esas', 'aquel', 'aquella',
    'sin', 'sobre', 'entre', 'hasta', 'desde', 'durante',
    'parece', 'creo', 'pienso', 'tengo', 'funciona'
}

# Sinónimos y palabras relacionadas para mejorar coincidencias
SINONIMOS = {
    'pc': 'cpu',
    'computador': 'cpu',
    'computadora': 'cpu',
    'ordenador': 'cpu',
    'equipo': 'cpu',
    'prende': 'enciende',
    'prender': 'enciende',
    'encender': 'enciende',
    'arranca': 'enciende',
    'arrancar': 'enciende',
    'inicia': 'enciende',
    'iniciar': 'enciende',
    'lenta': 'lento',
    'lentitud': 'lento',
    'despacio': 'lento',
    'trabada': 'lento',
    'trabado': 'lento',
    'colgada': 'lento',
    'colgado': 'lento',
    'atascada': 'atasco',
    'atascado': 'atasco',
    'atorada': 'atasco',
    'atorado': 'atasco',
    'papel': 'atasco',
    'caliente': 'sobrecalienta',
    'calentar': 'sobrecalienta',
    'calienta': 'sobrecalienta',
    'temperatura': 'sobrecalienta',
    'imprime': 'impresora',
    'imprimir': 'impresora',
    'impresión': 'impresora'
}

# Función para normalizar texto
def normalizar_texto(texto):
    # Convertir a minúsculas
    texto = texto.lower()
    # Eliminar caracteres especiales y números
    texto = re.sub(r'[^a-záéíóúñü\s]', '', texto)
    return texto

# Función para tokenizar texto (sin NLTK)
def tokenizar(texto):
    # Dividir por espacios y filtrar vacíos
    return [palabra.strip() for palabra in texto.split() if palabra.strip()]

# Función para reemplazar sinónimos
def reemplazar_sinonimos(palabras):
    return [SINONIMOS.get(palabra, palabra) for palabra in palabras]

# Función para tokenizar y eliminar palabras vacías
def procesar_entrada(texto):
    # Normalizar el texto
    texto_normalizado = normalizar_texto(texto)
    # Tokenizar el texto (sin NLTK)
    tokens = tokenizar(texto_normalizado)
    # Eliminar palabras vacías
    palabras_filtradas = [palabra for palabra in tokens if palabra not in PALABRAS_VACIAS]
    # Reemplazar sinónimos para mejorar coincidencias
    palabras_clave = reemplazar_sinonimos(palabras_filtradas)
    return palabras_clave

# Función para encontrar coincidencias con hechos
def encontrar_coincidencias(palabras_clave, hechos):
    for hecho in hechos:
        # Verificar si todas las palabras clave están en el hecho
        if all(palabra in hecho.lower() for palabra in palabras_clave):
            return hecho
    return "No se encontró un hecho coincidente."

# Ejemplo de uso
if __name__ == "__main__":
    hechos = [
        "La impresora no enciende",
        "La CPU está lenta",
        "La impresora tiene atascos de papel",
        "La CPU se sobrecalienta"
    ]

    entrada_usuario = "Mi impresora no funciona, parece que no enciende."
    palabras_clave = procesar_entrada(entrada_usuario)
    coincidencia = encontrar_coincidencias(palabras_clave, hechos)

    print(f"Entrada: {entrada_usuario}")
    print(f"Palabras clave: {palabras_clave}")
    print(f"Hecho coincidente: {coincidencia}")