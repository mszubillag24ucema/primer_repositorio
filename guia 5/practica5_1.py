sportsmen = []

# warm up


def save_sportsmen(sportsman, sport):
    sportsman_dict = {}
    sportsman_dict['sportsman'] = sportsman
    sportsman_dict['sport'] = sport

    sportsmen.append(sportsman_dict)


def print_sportsmen(lista_deportistas):
    for deportista_dict in lista_deportistas:
        print(f"El/La deportista {deportista_dict['sportsman']}, juega {deportista_dict['sport']}")


while True:
    print("(1) Agregar deportista")
    print("(2) Ver listado de deportistas")

    option = input(">> ")

    if option == "1":
        print("Nombre del deportista")
        sportsman = input(">> ")
        print("Deporte que practica")
        sport = input(">> ")

        save_sportsmen(sportsman, sport)
        # hice una función que me appendeee los datos a la lista

    if option == "2":
        print_sportsmen(sportsmen)

# Ejercicio 1

shopping_cart = []


def carrito_virtual(producto, q):
    cart_dict = {}
    cart_dict['producto'] = producto
    cart_dict['cantidad'] = q

    shopping_cart.append(cart_dict)


def buy_shopping_cart():
    for carrito in shopping_cart:
        print(f" Su carrito de compras es: \n {carrito['producto']} x {carrito['cantidad']} ")


while True:
    print("\t --------------")
    print("(1) Agregar productos a la lista")
    print("(2) Ver Carrito de Compras")
    print(" 3) Salir")
    print("----------------")
    option = input(">> ")

    if option == '3':
        break
    try:
        if int(option) == 1:
            print("¿Qué producto desea agregar?")
            producto = input(">> ")
            print("¿Qué cantidad?")
            q = int(nput(">> "))

            carrito_virtual(producto, q)

        elif int(option) == 2:
            buy_shopping_cart()

    except ValueError:
        print("Opcion invalida")