# Ejercicio 3
# MAKE IR WORK, MAKE IT BETTER
orders = []

while True:
    print("\n----------------------")
    print("\t 1) Agregar")
    print("\t 2) Listar")
    print("\t 3) Salir ")
    print("----------------------")
    option = input(">> ")

    if option == "3":
        break
    try:
        if option == "1":
            items = {}
            print("Name of the medicine:")
            medicine = input(">> ")
            print("Name of the laboratory:")
            lab = input(">> ")
            print("Quantity:")
            quantity = input(">> ")

            items["medicamento"] = medicine
            items["laboratorio"] = lab
            items["quantity"] = quantity

            for order in orders:
                # orders es la lista que tiene los diccionarios adentro
                # Hago este for para ver si agrego el medicamento o si ya existe
                if order["medicamento"] == items["medicamento"] and order["laboratorio"] == items["laboratorio"] and \
                        order["quantity"] == items["quantity"]:
                    print("The medicine already exists")
                else:
                    orders.append(items)

        elif option == "2":
            print(orders)

    except ValueError:
        print(f"The option {option} is not valid")

print("End of Program")
