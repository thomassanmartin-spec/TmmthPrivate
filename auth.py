import json
import os
import bcrypt

ARCHIVO = "usuarios.json"


def cargar_usuarios():
    if not os.path.exists(ARCHIVO):
        return {}
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def guardar_usuarios(usuarios):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=4)


def registrar(usuario, clave):
    usuarios = cargar_usuarios()
    if usuario in usuarios:
        return False
    hash_clave = bcrypt.hashpw(clave.encode(), bcrypt.gensalt())
    usuarios[usuario] = hash_clave.decode()
    guardar_usuarios(usuarios)
    return True


def login(usuario, clave):
    usuarios = cargar_usuarios()
    if usuario not in usuarios:
        return False
    return bcrypt.checkpw(clave.encode(), usuarios[usuario].encode())
