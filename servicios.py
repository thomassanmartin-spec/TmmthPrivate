import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY_CLIMA")
URL_CLIMA = "https://api.openweathermap.org/data/2.5/weather"
URL_INDICADORES = "https://mindicador.cl/api"


def obtener_clima(ciudad):
    parametros = {
        "q": ciudad,
        "appid": API_KEY,
        "units": "metric",
        "lang": "es"
    }
    try:
        respuesta = requests.get(URL_CLIMA, params=parametros, timeout=10)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            return {
                "temperatura": datos["main"]["temp"],
                "humedad": datos["main"]["humidity"],
                "estado": datos["weather"][0]["description"]
            }
        elif respuesta.status_code == 404:
            print("No encontré esa ciudad")
            return None
        else:
            return None
    except requests.exceptions.ConnectionError:
        print("No hay conexión, revisa tu internet")
        return None


def obtener_moneda(moneda):
    try:
        respuesta = requests.get(f"{URL_INDICADORES}/{moneda}", timeout=10)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            return datos["serie"][0]["valor"]
        return None
    except requests.exceptions.ConnectionError:
        print("No hay conexión, revisa tu internet")
        return None
