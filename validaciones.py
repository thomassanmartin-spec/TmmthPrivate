import re

MONEDAS = ["dolar", "euro", "uf"]


def texto_valido(texto):
    return texto is not None and texto.strip() != ""


def usuario_valido(usuario):
    return re.fullmatch(r"[a-zA-Z0-9_]{3,20}", usuario or "") is not None


def clave_valida(clave):
    return clave is not None and 8 <= len(clave) <= 50


def ciudad_valida(ciudad):
    if not texto_valido(ciudad) or len(ciudad) > 50:
        return False
    return ciudad.replace(" ", "").isalpha()


def moneda_valida(moneda):
    return moneda in MONEDAS


def monto_valido(monto):
    if re.fullmatch(r"[0-9]{1,9}", monto or "") is None:
        return False
    return 0 < int(monto) <= 100000000
