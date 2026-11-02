import json
import os
import bcrypt

ARCHIVO = "usuarios.json"


def cargar_usuarios():
    if not os.path.exists(ARCHIVO):
        return {}
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}


def guardar_usuarios(usuarios):
    try:
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            json.dump(usuarios, f, indent=4)
        return True
    except OSError:
        return False


def registrar(usuario, clave):
    usuarios = cargar_usuarios()
    if usuario in usuarios:
        return False
    hash_clave = bcrypt.hashpw(clave.encode(), bcrypt.gensalt())
    usuarios[usuario] = hash_clave.decode()
    return guardar_usuarios(usuarios)


def login(usuario, clave):
    usuarios = cargar_usuarios()
    if usuario not in usuarios:
        return False
    try:
        return bcrypt.checkpw(clave.encode(), usuarios[usuario].encode())
    except ValueError:
        return False
