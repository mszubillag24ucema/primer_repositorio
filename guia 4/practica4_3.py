laundry = []
costo = 3

while True:
    print("\n----------------------")
    print("\t 1) Lavandería")
    print("\t 2) Recepción")
    print("\t 3) Salir")
    print("----------------------")
    option = input(">> ")

    if option == "3":
        break
    try:
        if option == "1":
            service = {}
            print("Número de habitación:")
            room = input(">> ")
            print("Cantidad de prendas:")
            prendas = input(">> ")
            print("Fecha:")
            date = input(">> ")

            service["habitacion"] = room
            service["prendas"] = int(prendas)
            service["fecha"] = date

            laundry.append(service)

        if option == "2":
            print("Número de habitación:")
            room = input(">> ")
            numero = 0
            tickets = []
            resumen = {}
            fechas = []
            pago = numero * costo
            for servicio in laundry:

                if servicio["habitacion"] == room:
                    numero += servicio["prendas"]
                    resumen["habitacion"] = room
                    resumen["prendas"] = numero
                    fechas.append(servicio["fecha"])
                    resumen["fecha"] = fechas
                    tickets.append(resumen)
                    print(resumen)
                    print(f"Su total de prendas de lavandería es :")
                    print(f"{numero}")
                    print(f"El total por lavandería es: \n {numero * costo}")
                    payment = input("El cliente va a pagar?")
                    if payment == "si":
                        cuenta = int(input("ingrese monto:"))
                        laundry.remove(servicio)
                else:
                    print("El huesped no tiene cargos")

    except ValueError:
        print(f"The option {option} is not valid")
