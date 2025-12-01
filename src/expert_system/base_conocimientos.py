# Base de Conocimientos
# Este archivo contiene los hechos y reglas para el sistema experto.
# Optimizado para Raspberry Pi 3

# Hechos iniciales (problemas conocidos)
hechos = [
    "cpu no enciende",
    "cpu lento",
    "cpu sobrecalienta",
    "impresora no enciende",
    "impresora atasco",
    "impresora no imprime",
    "cpu ruido ventilador",
    "cpu pantalla azul",
    "cpu reinicia solo",
    "impresora manchas",
    "impresora lineas",
    "impresora wifi"
]

# Reglas con condiciones y acciones
reglas = [
    {
        "palabras_clave": ["cpu", "enciende"],
        "condicion": "cpu no enciende",
        "accion": """SOLUCIÓN - CPU NO ENCIENDE:
1. Verifique que el cable de alimentación esté bien conectado.
2. Compruebe que el interruptor de la fuente de poder esté encendido (I/O).
3. Revise si hay LEDs encendidos en la placa madre.
4. Pruebe con otro cable de alimentación o tomacorriente.
5. Si persiste, puede ser la fuente de poder dañada."""
    },
    {
        "palabras_clave": ["cpu", "lento"],
        "condicion": "cpu lento",
        "accion": """SOLUCIÓN - CPU LENTA:
1. Cierre programas innecesarios (Ctrl+Shift+Esc para ver procesos).
2. Verifique el uso de memoria RAM y disco.
3. Ejecute un análisis de antivirus.
4. Limpie archivos temporales (Ejecutar > %temp%).
5. Considere agregar más RAM o cambiar a SSD.
6. Desfragmente el disco duro si es HDD."""
    },
    {
        "palabras_clave": ["cpu", "sobrecalienta"],
        "condicion": "cpu sobrecalienta",
        "accion": """SOLUCIÓN - CPU SE SOBRECALIENTA:
1. Apague el equipo y deje enfriar.
2. Limpie los ventiladores y disipadores con aire comprimido.
3. Verifique que los ventiladores funcionen correctamente.
4. Reaplique pasta térmica si es necesario.
5. Mejore la ventilación del gabinete.
6. Considere agregar ventiladores adicionales."""
    },
    {
        "palabras_clave": ["impresora", "enciende"],
        "condicion": "impresora no enciende",
        "accion": """SOLUCIÓN - IMPRESORA NO ENCIENDE:
1. Verifique que el cable de alimentación esté conectado.
2. Pruebe con otro tomacorriente.
3. Revise si hay un interruptor de encendido.
4. Compruebe si hay LEDs indicadores.
5. Si tiene batería, verifique que esté cargada.
6. Si persiste, puede ser la fuente interna dañada."""
    },
    {
        "palabras_clave": ["impresora", "atasco"],
        "condicion": "impresora atasco",
        "accion": """SOLUCIÓN - ATASCO DE PAPEL:
1. Apague la impresora.
2. Abra todas las tapas de acceso.
3. Retire el papel atascado con cuidado (sin rasgarlo).
4. Verifique que no queden pedazos de papel.
5. Limpie los rodillos con un paño húmedo.
6. Use papel de buena calidad y bien almacenado.
7. No sobrecargue la bandeja de papel."""
    },
    {
        "palabras_clave": ["impresora", "imprime"],
        "condicion": "impresora no imprime",
        "accion": """SOLUCIÓN - IMPRESORA NO IMPRIME:
1. Verifique que la impresora esté encendida y en línea.
2. Revise la conexión USB o de red.
3. Compruebe los niveles de tinta/tóner.
4. Verifique que no haya trabajos en cola atascados.
5. Reinstale los controladores de la impresora.
6. Ejecute la herramienta de solución de problemas de Windows."""
    },
    {
        "palabras_clave": ["cpu", "ruido", "ventilador"],
        "condicion": "cpu ruido ventilador",
        "accion": """SOLUCIÓN - RUIDO EN VENTILADOR:
1. Limpie el ventilador con aire comprimido.
2. Verifique que no haya cables obstruyendo las aspas.
3. Lubrique el rodamiento del ventilador si es posible.
4. Considere reemplazar el ventilador si está desgastado.
5. Revise la configuración de velocidad del ventilador en BIOS."""
    },
    {
        "palabras_clave": ["cpu", "pantalla", "azul"],
        "condicion": "cpu pantalla azul",
        "accion": """SOLUCIÓN - PANTALLA AZUL (BSOD):
1. Anote el código de error que aparece.
2. Reinicie el equipo en Modo Seguro.
3. Actualice los controladores del sistema.
4. Ejecute el verificador de archivos del sistema (sfc /scannow).
5. Revise la memoria RAM con Windows Memory Diagnostic.
6. Verifique el disco duro con chkdsk /f /r."""
    },
    {
        "palabras_clave": ["cpu", "reinicia"],
        "condicion": "cpu reinicia solo",
        "accion": """SOLUCIÓN - CPU SE REINICIA SOLO:
1. Verifique la temperatura del procesador.
2. Revise la fuente de alimentación.
3. Compruebe la memoria RAM.
4. Actualice el BIOS si es necesario.
5. Revise el registro de eventos de Windows.
6. Desactive el reinicio automático para ver errores."""
    },
    {
        "palabras_clave": ["impresora", "manchas"],
        "condicion": "impresora manchas",
        "accion": """SOLUCIÓN - IMPRESORA DEJA MANCHAS:
1. Limpie los cabezales de impresión.
2. Ejecute la limpieza automática desde el software.
3. Verifique que el tóner/cartucho no esté dañado.
4. Limpie el tambor de la impresora (si aplica).
5. Use papel de buena calidad.
6. Reemplace el cartucho o tóner si es necesario."""
    },
    {
        "palabras_clave": ["impresora", "lineas"],
        "condicion": "impresora lineas",
        "accion": """SOLUCIÓN - IMPRESORA IMPRIME CON LÍNEAS:
1. Ejecute la alineación de cabezales.
2. Limpie los cabezales de impresión.
3. Verifique los niveles de tinta.
4. Ejecute múltiples ciclos de limpieza.
5. Reemplace el cartucho si está obstruido.
6. Revise si hay suciedad en el cristal del escáner."""
    },
    {
        "palabras_clave": ["impresora", "wifi"],
        "condicion": "impresora wifi",
        "accion": """SOLUCIÓN - PROBLEMAS DE CONEXIÓN WIFI:
1. Verifique que la impresora esté conectada a la red correcta.
2. Reinicie el router y la impresora.
3. Acerque la impresora al router.
4. Vuelva a configurar la conexión WiFi.
5. Actualice el firmware de la impresora.
6. Verifique que no haya interferencias de otros dispositivos."""
    }
]

# Función para obtener una acción basada en palabras clave
def obtener_accion(palabras_clave):
    mejor_coincidencia = None
    max_coincidencias = 0
    
    for regla in reglas:
        # Contar cuántas palabras clave coinciden
        coincidencias = sum(1 for palabra in palabras_clave 
                          if any(palabra in kw for kw in regla["palabras_clave"]))
        
        if coincidencias > max_coincidencias:
            max_coincidencias = coincidencias
            mejor_coincidencia = regla
    
    if mejor_coincidencia and max_coincidencias > 0:
        return mejor_coincidencia["accion"]
    
    return """No se encontró una solución específica para el problema.
    
Por favor, intente describir el problema con más detalle.
Ejemplos de problemas que puedo resolver:
- "Mi CPU no enciende"
- "La impresora está lenta"
- "Hay un atasco de papel"
- "La computadora se sobrecalienta"
- "La impresora no imprime"
"""

# Ejemplo de uso
if __name__ == "__main__":
    problema = ["cpu", "lento"]
    solucion = obtener_accion(problema)
    print(f"Problema: {problema}\nSolución: {solucion}")