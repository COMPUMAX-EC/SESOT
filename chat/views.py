from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import json
import sys
import os

# Agregar src al path para importar el motor experto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'src'))

def index(request):
    """Renderiza la interfaz de chat"""
    return render(request, 'chat/index.html')

@csrf_exempt
def diagnose(request):
    """
    Endpoint API para procesar mensajes del chat
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message = data.get('message', '').strip()
            
            # Procesar con el sistema experto
            response = get_expert_response(message)
            
            return JsonResponse({
                'success': True,
                'response': response,
                'timestamp': timezone.now().isoformat()
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=500)
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)

def get_expert_response(input_text):
    """
    Lógica del sistema experto - Procesa mensajes y retorna diagnósticos
    """
    lower = input_text.lower()
    
    # DETECCIÓN DE DISPOSITIVO
    if any(word in lower for word in ['cpu', 'computadora', 'pc', 'equipo', 'ordenador']):
        return {
            'type': 'question',
            'content': '🖥️ **Diagnóstico de CPU iniciado**\n\n¿El equipo enciende? (se ven luces o escuchas ventiladores)',
            'device': 'cpu'
        }
    
    if any(word in lower for word in ['impresora', 'printer']):
        return {
            'type': 'question',
            'content': '🖨️ **Diagnóstico de Impresora iniciado**\n\n¿Cuál es el problema específico?\n• No imprime\n• Imprime con manchas\n• Atasco de papel',
            'device': 'impresora'
        }
    
    # DIAGNÓSTICOS CPU
    if ('no' in lower) and any(word in lower for word in ['enciende', 'prende', 'energía', 'energia']):
        return {
            'type': 'diagnosis',
            'content': '⚡ **DIAGNÓSTICO:** Fallo de Alimentación Eléctrica\n\n**CAUSA:** Fuente de poder dañada o cable en mal estado\n\n**SOLUCIÓN:**\n✓ Verifica que el cable de poder esté conectado firmemente\n✓ Prueba con otro cable de poder certificado\n✓ Si persiste, la fuente de poder está dañada\n\n💡 **COSTO APROXIMADO:** $25-45 fuente genérica, $60-120 fuente certificada',
            'device': 'cpu',
            'solution': 'Reemplazar fuente de poder'
        }
    
    if ('si' in lower or 'sí' in lower) and any(word in lower for word in ['enciende', 'prende']):
        return {
            'type': 'question',
            'content': '✅ El equipo recibe energía correctamente.\n\n**Siguiente verificación:**\n¿Aparece imagen en el monitor? (¿da video?)',
            'device': 'cpu'
        }
    
    if ('no' in lower) and ('video' in lower or 'imagen' in lower or 'pantalla' in lower):
        return {
            'type': 'diagnosis',
            'content': '🔧 **DIAGNÓSTICO:** Fallo en POST (Power-On Self-Test)\n\n**CAUSA PRINCIPAL:** Memoria RAM sucia o mal conectada\n\n**SOLUCIÓN PASO A PASO:**\n1️⃣ Apaga y desconecta el equipo\n2️⃣ Abre el case (lateral)\n3️⃣ Localiza las memorias RAM (módulos rectangulares en slots)\n4️⃣ Presiona los seguros laterales y retíralas\n5️⃣ Limpia los contactos dorados con goma de borrar blanca\n6️⃣ Sopla suavemente los slots\n7️⃣ Reinserta las memorias hasta escuchar "click"\n8️⃣ Enciende el equipo\n\n⚠️ **Si persiste:** Podría ser tarjeta gráfica o placa madre',
            'device': 'cpu',
            'solution': 'Limpieza de RAM'
        }
    
    if ('si' in lower or 'sí' in lower) and ('video' in lower or 'imagen' in lower):
        return {
            'type': 'diagnosis',
            'content': '💻 **DIAGNÓSTICO:** Hardware Funcional - Problema de Software\n\n**CAUSA:** Sistema Operativo corrupto o Disco Duro dañado\n\n**VERIFICACIÓN:**\n1. Reinicia el equipo\n2. Presiona F2/DEL/F10 al encender (depende de la marca)\n3. Intenta entrar a la BIOS\n\n**RESULTADO:**\n✓ **SI entra a BIOS:** Sistema operativo dañado → Reinstalar Windows\n✗ **NO entra a BIOS:** Disco duro dañado → Reemplazar disco\n\n💾 **RECOMENDACIÓN:** Migrar a SSD ($30-50 por 240GB)',
            'device': 'cpu',
            'solution': 'Reinstalar SO o cambiar disco'
        }
    
    # DIAGNÓSTICOS IMPRESORA
    if 'no imprime' in lower or 'no sale' in lower or 'no funciona' in lower:
        return {
            'type': 'diagnosis',
            'content': '🔌 **DIAGNÓSTICO:** Problema de Conectividad/Drivers\n\n**SOLUCIONES EN ORDEN:**\n\n**NIVEL 1 - Conexión:**\n✓ Cable USB bien conectado (probar otro puerto)\n✓ Impresora encendida (luz verde fija)\n✓ Probar con otro cable USB\n\n**NIVEL 2 - Cola de impresión:**\n1. Panel de Control → Dispositivos e Impresoras\n2. Click derecho en tu impresora → "Ver cola de impresión"\n3. Menú "Impresora" → Cancelar todos los documentos\n4. Reiniciar el Spooler: Win+R → services.msc → Buscar "Cola de impresión" → Reiniciar\n\n**NIVEL 3 - Drivers:**\n• Desinstalar impresora completamente\n• Descargar drivers desde web del fabricante\n• Instalar en modo administrador',
            'device': 'impresora',
            'solution': 'Verificar conexión y drivers'
        }
    
    if 'mancha' in lower or 'sucio' in lower or 'borroso' in lower:
        return {
            'type': 'diagnosis',
            'content': '💧 **DIAGNÓSTICO:** Cabezales de Impresión Obstruidos\n\n**TIPO DE IMPRESORA:**\n\n**📊 INYECCIÓN DE TINTA:**\n1. Software de impresora → Mantenimiento → "Limpieza de cabezales"\n2. Ejecutar 2-3 ciclos (consume tinta)\n3. Imprimir página de prueba\n4. Si persiste: Limpieza profunda (manual)\n\n**🖨️ LÁSER:**\n• Problema: Tóner bajo o tambor rayado\n• Solución: Agitar cartucho, si persiste reemplazar\n\n**LIMPIEZA MANUAL (AVANZADO):**\n• Algodón + Alcohol isopropílico 90%\n• Limpiar inyectores suavemente\n• Dejar secar 10 minutos',
            'device': 'impresora',
            'solution': 'Limpieza de cabezales'
        }
    
    if 'atasco' in lower or 'papel' in lower or 'atorada' in lower or 'trabada' in lower:
        return {
            'type': 'diagnosis',
            'content': '📄 **DIAGNÓSTICO:** Atasco de Papel (Paper Jam)\n\n**PROCEDIMIENTO CORRECTO:**\n\n**1. APAGAR impresora** (importante para no dañar rodillos)\n\n**2. LOCALIZAR el papel:**\n• Abrir todas las tapas (frontal, posterior, superior)\n• Usar linterna si es necesario\n\n**3. RETIRAR con cuidado:**\n⚠️ SIEMPRE jalar en dirección de los rodillos (hacia adelante)\n⚠️ NUNCA jalar hacia atrás\n• Tirar firme pero suave\n• Si se rompe, sacar todos los pedazos\n\n**4. VERIFICAR:**\n• Rodillos limpios (sin papelitos)\n• Bandeja de papel correctamente ajustada\n• Papel en buen estado (no húmedo/arrugado)\n\n**5. ENCENDER** y hacer impresión de prueba\n\n**PREVENCIÓN:**\n✓ Papel de buena calidad\n✓ No sobrecargar la bandeja\n✓ Ajustar guías correctamente',
            'device': 'impresora',
            'solution': 'Retirar obstrucción'
        }
    
    # RESPUESTA POR DEFECTO
    return {
        'type': 'question',
        'content': '👋 ¡Hola! Soy el **Sistema Experto de Soporte Técnico (SESOT)**.\n\nPuedo ayudarte a diagnosticar problemas de hardware.\n\n**¿Qué dispositivo presenta problemas?**\n\n🖥️ **Computadora/CPU**\n🖨️ **Impresora**\n\nEscribe el tipo de dispositivo o describe el problema directamente.',
        'device': None
    }