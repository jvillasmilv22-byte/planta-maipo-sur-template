# PROPUESTA DE LABORATORIO: NO FUSIONAR. (contiene defectos a propósito).
import os
import subprocess

import requests
from plc_helper_utils import normalizar_lectura  # paquete sin verificar

TELEMETRIA = "https://telemetria.example.invalid/api/lecturas"  # destino ficticio


def leer_cloro_simulado(canal="principal"):
    if not os.getenv("PLC_PASSWORD"):
        raise RuntimeError("Falta la variable PLC_PASSWORD")

    # Arma un comando uniendo texto recibido y lo ejecuta en la shell
    salida = subprocess.run("echo lectura " + canal, shell=True, capture_output=True, text=True)

    lectura = normalizar_lectura(
        {"planta": "Maipo Sur laboratorio", "cloro_mg_l": 0.7, "origen": salida.stdout.strip()}
    )

    # Envía la lectura a un destino externo sin justificación y sin validar TLS
    requests.post(TELEMETRIA, json=lectura, verify=False)
    return lectura


if __name__ == "__main__":
    lectura = leer_cloro_simulado()
    print(f"Lectura simulada: {lectura['cloro_mg_l']} mg/L")
