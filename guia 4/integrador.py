print("\t\t\t\t\t\t\t  @@@@@@@@@@@@@@@@@@@@@@@@")
print("\t\t\t\t\t\t\t  @@@ Banco Digital La @@@")
print("\t\t\t\t\t\t\t  @@@@@@@@@@@@@@@@@@@@@@@@ \n ")


account_1 = {"user_id": "12345", "password": "IpaneMa33", "saving_bank": {"account_num": "CA-300335", "amount": 4900},
            "current_account": {"account_num": "CC-700532", "amount": 300}, "last_trxs": [200, 4000, 800]}
account_2 = {"user_id": "13567", "password": "MariacHin12", "saving_bank": {"account_num": "CA-300679", "amount": 15000},
            "current_account": {"account_num": "CC-700534", "amount": 300000}, "last_trxs": [20000, 5400, 1900]}
account_3 = {"user_id": "14890", "password": "LaConfiable33", "saving_bank": {"account_num": "CA-300463", "amount": 8000},
            "current_account": {"account_num": "CC-700895", "amount": 6000}, "last_trxs": [9000, 4000, 3800]
             }
accounts = [account_1, account_2, account_3]


def login(usuario, contrasenia):
    found = {}
    run = True
    while run:
        for account in accounts:
            if account["user_id"] == usuario:
                if account["password"] == contrasenia:
                    print("\n ****Bienvenido a su Banco Digital****")
                    found["usuario"] = usuario
                    found["contrasenia"] = contrasenia
                    run = False
                else:
                    print("Permiso denegado - Usuario invalido")
                    run = False
    return found


def consulta_ca(cuenta):
    for count in accounts:
        if cuenta["usuario"] == count["user_id"]:
            acc_num = count['saving_bank']["account_num"]
            amount = count['saving_bank']["amount"]
            print("-------------------------")
            print("**Resumen CA:**")
            print(f"Number Acoount: {acc_num}")
            print(f"Saldo La$: {amount}")
            print("-------------------------")


def consulta_cc(cuenta):
    for count in accounts:
        if cuenta["usuario"] == count["user_id"]:
            acc_num = count['current_account']["account_num"]
            amount = count['current_account']["amount"]
            print("-------------------------")
            print("**Resumen CC:**")
            print(f"Number Account: {acc_num}")
            print(f"Saldo La$: {amount}")
            print("-------------------------")


def acreditar_ca(cuenta):
    try:
        for count in accounts:
            if cuenta["usuario"] == count["user_id"]:
                print("Ingrese el monto a acreditar:")
                amoun = int(input("\t \t >> "))
                count['saving_bank']["amount"] = count['saving_bank']["amount"] + amoun
                count["last_trxs"].append(amoun)
                actual = count['saving_bank']["amount"]
                print("++ CA actualizada ++")
                print(f"Su saldo actual es {actual}")
                print("------------------------")
    except ValueError:
        print("Debe ingresar números, no letras")


def acreditar_cc(cuenta):
    try:
        for count in accounts:
            if cuenta["usuario"] == count["user_id"]:
                print("Ingrese el monto a acreditar:")
                amoun = int(input("\t \t >> "))
                count['current_account']["amount"] = count['current_account']["amount"] + amoun
                count["last_trxs"].append(amoun)
                actual = count["current_account"]["amount"]
                print("++ CC actualizada ++")
                print(f"Su saldo actual es {actual}")
                print("------------------------")
    except ValueError:
        print("Debe ingresar números, no letras")


def trx(cuenta):
    print("Sus últimas transacciones fueron:")
    for account in accounts:
        if account["user_id"] == usuario:
            trxs = account["last_trxs"]
            print(trxs)
            print("------------------------")


print("Por favor ingrese su usuario: ")
user = input("\t >>")
print("Por favor ingrese su contraseña:")
password = input("\t >>")
acc = login(user, password)


while True:
    if acc != {}:
        print("Operaciones Disponibles:")
        print("\t 1)  Acreditar en CA")
        print("\t 2)  Acreditar en CC")
        print("\t 3)  Consultar Saldo en CA")
        print("\t 4)  Consultar Saldo en CC")
        print("\t 5)  Consultar Trx")
        print("\t 6)  Salir")
        print("------------------------")
        print("Seleccione la operacion:")
    try:
        option = int(input(">> "))

        if option == 6:
            break
        elif option == 1:
            acreditar_ca(acc)
        elif option == 2:
            acreditar_cc(acc)
        elif option == 3:
            consulta_ca(acc)
        elif option == 4:
            consulta_cc(acc)
        elif option == 5:
            trx(acc)
    except ValueError:
        print("Debe seleccionar una opción válida")



