import os
import sys

# Agregamos la ruta raíz al sistema para que encuentre lector_cloro
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lector_cloro import leer_cloro_simulado

os.environ.setdefault("PLC_PASSWORD", "VALOR-FICTICIO-DE-PRUEBA")
resultado = leer_cloro_simulado()
assert resultado["cloro_mg_l"] == 0.7
print("Prueba funcional correcta; el secreto no fue mostrado")
