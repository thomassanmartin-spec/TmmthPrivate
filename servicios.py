import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY_CLIMA")
URL_CLIMA = "https://api.openweathermap.org/data/2.5/weather"
URL_INDICADORES = "https://mindicador.cl/api"


def consultar(url, parametros=None):
    try:
        respuesta = requests.get(url, params=parametros, timeout=10)
    except requests.exceptions.Timeout:
        print("Se demoro mucho")
        return None
    except requests.exceptions.ConnectionError:
        print("Sin internet")
        return None
    except requests.exceptions.RequestException:
        print("Algo fallo")
        return None

    if respuesta.status_code == 200:
        try:
            return respuesta.json()
        except ValueError:
            print("Llegaron datos raros")
            return None

    if respuesta.status_code == 401:
        print("La llave no sirve")
    elif respuesta.status_code == 404:
        print("No lo encontre")
    elif respuesta.status_code == 429:
        print("Muchas consultas espera un rato")
    elif respuesta.status_code >= 500:
        print("El servicio esta caido")
    else:
        print("Algo fallo")
    return None


def obtener_clima(ciudad):
    if not API_KEY:
        print("Falta la llave del clima")
        return None

    parametros = {
        "q": ciudad,
        "appid": API_KEY,
        "units": "metric",
        "lang": "es"
    }
    datos = consultar(URL_CLIMA, parametros)
    if not datos:
        return None

    try:
        return {
            "temperatura": float(datos["main"]["temp"]),
            "humedad": datos["main"]["humidity"],
            "estado": datos["weather"][0]["description"]
        }
    except (KeyError, IndexError, TypeError, ValueError):
        print("Llegaron datos raros")
        return None


def obtener_moneda(moneda):
    datos = consultar(f"{URL_INDICADORES}/{moneda}")
    if not datos:
        return None

    try:
        valor = float(datos["serie"][0]["valor"])
    except (KeyError, IndexError, TypeError, ValueError):
        print("Llegaron datos raros")
        return None

    if valor <= 0:
        print("Llegaron datos raros")
        return None
    return valor
