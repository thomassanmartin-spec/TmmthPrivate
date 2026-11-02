import json
import os
from datetime import datetime

ARCHIVO = "historial.json"


def cargar_historial():
    if not os.path.exists(ARCHIVO):
        return []
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []


def guardar_consulta(usuario, tipo, dato, resultado):
    historial = cargar_historial()
    historial.append({
        "usuario": usuario,
        "tipo": tipo,
        "dato": dato,
        "resultado": resultado,
        "fecha": datetime.now().strftime("%d-%m-%Y %Hh%M")
    })
    try:
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            json.dump(historial, f, indent=4, ensure_ascii=False)
    except OSError:
        print("No se pudo guardar")


def ver_historial(usuario):
    consultas = [c for c in cargar_historial() if c.get("usuario") == usuario]
    if not consultas:
        print("No hay nada todavia")
        return
    for c in consultas[-10:]:
        print(f"{c['fecha']} {c['tipo']} {c['dato']} {c['resultado']}")
