# Exercise 2
vehicles = {
    "moto": 10,
    "auto": 20,
    "camioneta": 25,
    "camion": 60,
    "camion_con_acoplado": 90,
    "emmet brown": 200}

# ES MEJOR SI HAGO UN DICCIONARIO EN VEZ DE VARIBALES


def ticket(category):
    price = vehicles[category]
    print("************************************")
    print("Imprimiendo....\t")
    print(f"Vehículo {category.upper()}, tarifa ${price}")
    print("************************************\n")


def menu():
    while True:
        print("#################################")
        print(" \t 1) moto \n \t 2) auto \n \t 3) camioneta \n \t 4) camion \n \t 5) camion_con_acoplado"
              "\n \t 6) Emmet Brown")
        print("#################################\n")
        category = input(">>")

        if category == "1":
            ticket("moto")
        elif category == "2":
            ticket("auto")
        elif category == "3":
            ticket("camioneta")
        elif category == "4":
            ticket("camion")
        elif category == "5":
            ticket("camion_con_acoplado")
        elif category == "6":
            ticket("emmet brown")
        else:
            print("Opción inválida")


menu()
