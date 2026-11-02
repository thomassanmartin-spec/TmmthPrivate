from getpass import getpass
from auth import login, registrar
from servicios import obtener_clima, obtener_moneda
from validaciones import texto_valido, ciudad_valida, moneda_valida


def calcular_pago(sueldo, moneda):
    pass


def menu_principal(usuario):
    while True:
        print("\n--- Menú ---")
        print("1. Clima")
        print("2. Monedas")
        print("3. Pago")
        print("4. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            ciudad = input("Ciudad: ")
            if not ciudad_valida(ciudad):
                print("Ciudad mala")
                continue
            clima = obtener_clima(ciudad)
            if clima:
                print(f"Temp: {clima['temperatura']}°")
                print(f"Humedad: {clima['humedad']}%")
                print(clima['estado'])
        elif opcion == "2":
            moneda = input("dolar, euro o uf: ").lower()
            if not moneda_valida(moneda):
                print("Moneda mala")
                continue
            valor = obtener_moneda(moneda)
            if valor:
                print(f"${valor}")
        elif opcion == "3":
            print("Aún no")
        elif opcion == "4":
            print("Chao")
            break
        else:
            print("No existe")


def inicio():
    print("1. Entrar")
    print("2. Crear usuario")
    opcion = input("Opción: ")

    usuario = input("Usuario: ")
    clave = getpass("Clave: ")

    if not texto_valido(usuario) or not texto_valido(clave):
        print("Faltan datos")
        return

    if opcion == "1":
        if login(usuario, clave):
            print("Hola")
            menu_principal(usuario)
        else:
            print("Datos malos")
    elif opcion == "2":
        if registrar(usuario, clave):
            print("Listo")
        else:
            print("Ya existe")


if __name__ == "__main__":
    inicio()
