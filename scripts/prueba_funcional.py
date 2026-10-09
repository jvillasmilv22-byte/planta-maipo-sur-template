import os
from lector_cloro import leer_cloro_simulado

os.environ.setdefault("PLC_PASSWORD", "VALOR-FICTICIO-DE-PRUEBA")
resultado = leer_cloro_simulado()
assert resultado["cloro_mg_l"] == 0.7
print("Prueba funcional correcta; el secreto no fue mostrado")
