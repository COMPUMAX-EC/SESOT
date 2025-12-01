import sys
import os
import collections
import collections.abc

# Agregamos el directorio 'src' al path para que Python encuentre el paquete 'expert_system'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Parche para compatibilidad con Python 3.10+ (experta/frozendict usan collections.Mapping que fue eliminado)
if not hasattr(collections, "Mapping"):
    collections.Mapping = collections.abc.Mapping

from expert_system.engine import SoporteTecnico

def main():
    # Instanciamos el motor
    engine = SoporteTecnico()
    
    while True:
        # 1. Reset: Borra la Memoria de Trabajo anterior (olvida la consulta previa)
        engine.reset()
        
        # 2. Run: Inicia el ciclo Match-Resolve-Act
        engine.run()
        
        # Opción para salir del bucle infinito
        print("-" * 40)
        if input("¿Nueva consulta? (s/n): ").lower() != 's':
            break

if __name__ == "__main__":
    main()