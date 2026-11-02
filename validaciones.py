def texto_valido(texto):
    if texto is None:
        return False
    return texto.strip() != ""


def ciudad_valida(ciudad):
    if not texto_valido(ciudad):
        return False
    return ciudad.replace(" ", "").isalpha()


def moneda_valida(moneda):
    return moneda in ["dolar", "euro", "uf"]


def monto_valido(monto):
    pass
