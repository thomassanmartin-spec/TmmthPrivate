from getpass import getpass
from auth import login, registrar
from servicios import obtener_clima, obtener_moneda
from validaciones import texto_valido, ciudad_valida, moneda_valida


def calcular_pago(sueldo, moneda):
    pass


def menu_principal(usuario):
    while True:
        print(f"\n--- EcoTech Solutions | {usuario} ---")
        print("1. Ver clima")
        print("2. Ver tipo de cambio")
        print("3. Calcular pago")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            ciudad = input("Ciudad: ")
            if not ciudad_valida(ciudad):
                print("Ojo, esa ciudad no es válida")
                continue
            clima = obtener_clima(ciudad)
            if clima:
                print(f"Temperatura: {clima['temperatura']} °C")
                print(f"Humedad: {clima['humedad']} %")
                print(f"Estado: {clima['estado']}")
        elif opcion == "2":
            moneda = input("Moneda (dolar, euro, uf): ").lower()
            if not moneda_valida(moneda):
                print("Esa moneda no la tengo")
                continue
            valor = obtener_moneda(moneda)
            if valor:
                print(f"1 {moneda} = ${valor} CLP")
        elif opcion == "3":
            print("Todavía no está listo")
        elif opcion == "4":
            print("Ya, nos vemos")
            break
        else:
            print("Opción no válida")


def inicio():
    print("1. Iniciar sesión")
    print("2. Registrarse")
    opcion = input("Elige una opción: ")

    usuario = input("Usuario: ")
    clave = getpass("Clave: ")

    if not texto_valido(usuario) or not texto_valido(clave):
        print("No puedes dejar campos vacíos")
        return

    if opcion == "1":
        if login(usuario, clave):
            print("Listo, entraste")
            menu_principal(usuario)
        else:
            print("Usuario o clave incorrectos")
    elif opcion == "2":
        if registrar(usuario, clave):
            print("Usuario creado, ahora inicia sesión")
        else:
            print("Ese usuario ya existe")


if __name__ == "__main__":
    inicio()
