from getpass import getpass
from auth import login, registrar
from servicios import obtener_clima, obtener_moneda
from historial import guardar_consulta, ver_historial
from validaciones import (
    texto_valido,
    usuario_valido,
    clave_valida,
    ciudad_valida,
    moneda_valida,
    monto_valido
)

INTENTOS = 3
NOMBRES = {"dolar": "dolares", "euro": "euros", "uf": "UF"}


def revisar_clima(clima):
    estado = clima["estado"].lower()
    if "lluvia" in estado or "tormenta" in estado or "nieve" in estado:
        return "Mejor no trabajar afuera hoy"
    if clima["temperatura"] > 35 or clima["temperatura"] < 0:
        return "Ojo con la temperatura"
    return "Se puede trabajar sin problema"


def calcular_pago(sueldo, valor):
    return round(sueldo / valor)


def pedir_moneda():
    moneda = input("dolar euro o uf ").strip().lower()
    if not moneda_valida(moneda):
        print("Moneda mala")
        return None
    return moneda


def opcion_clima(usuario):
    ciudad = input("Ciudad ").strip()
    if not ciudad_valida(ciudad):
        print("Ciudad mala")
        return
    clima = obtener_clima(ciudad)
    if clima:
        temperatura = round(clima["temperatura"])
        print(f"Temperatura {temperatura}°")
        print(f"Humedad {clima['humedad']}%")
        print(f"Cielo {clima['estado']}")
        print(revisar_clima(clima))
        guardar_consulta(usuario, "clima", ciudad, f"{temperatura}°")


def opcion_moneda(usuario):
    moneda = pedir_moneda()
    if not moneda:
        return
    valor = obtener_moneda(moneda)
    if valor:
        print(f"1 {moneda} son ${round(valor)}")
        guardar_consulta(usuario, "moneda", moneda, f"${round(valor)}")


def opcion_pago(usuario):
    sueldo = input("Sueldo en pesos ").strip()
    if not monto_valido(sueldo):
        print("Monto malo")
        return
    moneda = pedir_moneda()
    if not moneda:
        return
    valor = obtener_moneda(moneda)
    if valor:
        pago = calcular_pago(int(sueldo), valor)
        print(f"Son {pago} {NOMBRES[moneda]}")
        guardar_consulta(usuario, "pago", f"${sueldo}", f"{pago} {NOMBRES[moneda]}")


def menu_principal(usuario):
    while True:
        print("\nMENU")
        print("1 Clima")
        print("2 Monedas")
        print("3 Pago")
        print("4 Historial")
        print("5 Salir")
        opcion = input("Opcion ").strip()

        if opcion == "1":
            opcion_clima(usuario)
        elif opcion == "2":
            opcion_moneda(usuario)
        elif opcion == "3":
            opcion_pago(usuario)
        elif opcion == "4":
            ver_historial(usuario)
        elif opcion == "5":
            print("Chao")
            break
        else:
            print("No existe")


def entrar():
    for _ in range(INTENTOS):
        usuario = input("Usuario ").strip()
        clave = getpass("Clave ")
        if not texto_valido(usuario) or not texto_valido(clave):
            print("Faltan datos")
            continue
        if login(usuario, clave):
            print(f"Hola {usuario}")
            return usuario
        print("Datos malos")
    print("Muchos intentos")
    return None


def crear_usuario():
    usuario = input("Usuario ").strip()
    if not usuario_valido(usuario):
        print("Usuario malo solo letras y numeros")
        return
    clave = getpass("Clave ")
    if not clave_valida(clave):
        print("La clave debe tener minimo 8")
        return
    if getpass("Repite la clave ") != clave:
        print("No son iguales")
        return
    if registrar(usuario, clave):
        print("Listo ya puedes entrar")
    else:
        print("Ese usuario ya existe")


def inicio():
    while True:
        print("\n1 Entrar")
        print("2 Crear usuario")
        print("3 Salir")
        opcion = input("Opcion ").strip()

        if opcion == "1":
            usuario = entrar()
            if usuario:
                menu_principal(usuario)
            return
        elif opcion == "2":
            crear_usuario()
        elif opcion == "3":
            print("Chao")
            return
        else:
            print("No existe")


if __name__ == "__main__":
    try:
        inicio()
    except KeyboardInterrupt:
        print("\nChao")
    except Exception:
        print("Algo fallo")
