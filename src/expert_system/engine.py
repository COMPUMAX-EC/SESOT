from experta import *

class SoporteTecnico(KnowledgeEngine):
    """
    Motor de inferencia basado en reglas para diagnóstico de hardware.
    Maneja la lógica de decisión usando el algoritmo Rete.
    """

    # 1. INICIALIZACIÓN DE LA MEMORIA DE TRABAJO
    @DefFacts()
    def _inicializar(self):
        """
        Carga los hechos iniciales en la memoria de trabajo al arrancar el motor.
        Equivalente a 'encender' el sistema.
        """
        print("\n--- INICIANDO SISTEMA EXPERTO (SESOT) ---")
        yield Fact(action='elegir_dispositivo')

    # 2. REGLAS DE CONTROL DE FLUJO (Preguntas)
    
    @Rule(Fact(action='elegir_dispositivo'))
    def input_dispositivo(self):
        """
        Primera interacción: Determina la rama del árbol (CPU vs Impresora).
        """
        print("¿Qué dispositivo deseas diagnosticar?")
        # Validamos entrada básica para evitar errores sucios
        tipo = ""
        while tipo not in ['cpu', 'impresora']:
            tipo = input("Escribe 'cpu' o 'impresora': ").lower().strip()
        
        # AQUÍ OCURRE LA MAGIA:
        # Declaramos un hecho. Esto cambia el estado del sistema y disparará nuevas reglas.
        self.declare(Fact(dispositivo=tipo))

    # --- RAMA: IMPRESORAS ---
    
    @Rule(Fact(dispositivo='impresora'))
    def input_sintoma_impresora(self):
        print("\n[RAMA IMPRESORA ACTIVADA]")
        sintoma = input("¿Cuál es el fallo? (no imprime / mancha / atasco): ").lower().strip()
        self.declare(Fact(sintoma=sintoma))

    # --- RAMA: CPU ---

    @Rule(Fact(dispositivo='cpu'))
    def input_sintoma_cpu(self):
        print("\n[RAMA CPU ACTIVADA]")
        enciende = input("¿El equipo enciende (ventiladores/luces)? (si/no): ").lower().strip()
        self.declare(Fact(enciende=enciende))

    # Sub-rama CPU: Si enciende, preguntar por video
    @Rule(Fact(dispositivo='cpu'), Fact(enciende='si'))
    def input_video_cpu(self):
        video = input("¿Da video en el monitor? (si/no): ").lower().strip()
        self.declare(Fact(video=video))

    # 3. REGLAS DE CONOCIMIENTO (Diagnósticos Finales)
    # Estas reglas son las "hojas" del árbol. No preguntan, solo concluyen.

    # Diagnósticos Impresora
    @Rule(Fact(dispositivo='impresora'), Fact(sintoma='no imprime'))
    def diag_imp_conexion(self):
        print("\n>>> DIAGNÓSTICO: Fallo de Conectividad o Cola de Impresión.")
        print(">>> ACCIÓN: 1. Revisa el cable USB. 2. Borra la cola de impresión en Windows.")

    @Rule(Fact(dispositivo='impresora'), Fact(sintoma='mancha'))
    def diag_imp_cabezales(self):
        print("\n>>> DIAGNÓSTICO: Suciedad en inyectores o rodillos.")
        print(">>> ACCIÓN: Ejecuta la limpieza de cabezales desde el software de la marca.")

    @Rule(Fact(dispositivo='impresora'), Fact(sintoma='atasco'))
    def diag_imp_papel(self):
        print("\n>>> DIAGNÓSTICO: Obstrucción mecánica.")
        print(">>> ACCIÓN: Abre las tapas y retira el papel tirando suavemente en dirección de los rodillos.")

    # Diagnósticos CPU
    @Rule(Fact(dispositivo='cpu'), Fact(enciende='no'))
    def diag_cpu_energia(self):
        print("\n>>> DIAGNÓSTICO: Fallo de Alimentación Eléctrica.")
        print(">>> ACCIÓN: Fuente de poder quemada o cable dañado. Prueba con otro cable de poder.")

    @Rule(Fact(dispositivo='cpu'), Fact(enciende='si'), Fact(video='no'))
    def diag_cpu_ram(self):
        print("\n>>> DIAGNÓSTICO: Fallo de POST (Power On Self Test).")
        print(">>> ACCIÓN: Probablemente RAM sucia. Limpia los contactos dorados de la RAM con un borrador.")

    @Rule(Fact(dispositivo='cpu'), Fact(enciende='si'), Fact(video='si'))
    def diag_cpu_software(self):
        print("\n>>> DIAGNÓSTICO: Hardware funcional.")
        print(">>> ACCIÓN: El problema es el Sistema Operativo o el Disco Duro. Intenta entrar a la BIOS.")

    # 4. MANEJO DE ERRORES (Regla Default)
    # salience=-1 asegura que esta regla sea la última en probarse
    @Rule(AS.f << Fact(dispositivo=MATCH.d), salience=-1)
    def desconocido(self, d, f):
        # Esta regla atrapa casos donde declaramos un dispositivo pero no coincidió ninguna regla de síntomas
        # Es útil para debug
        pass