# Ejercicio 5 - Cajero automatico

import os

account_1 = {
	"user_id": "05561",
	"password": "pass123",
	"saving_bank": {
		"account_num": "009911",
		"amount": 4200.0
	},
	"current_account": {
		"account_num": "009921",
		"amount": 500.0
	},
	"last_trxs": [120.0, 302.1, 892.4]
}

account_2 = {
	"user_id": "04421",
	"password": "pass321",
	"saving_bank": {
		"account_num": "009912",
		"amount": 1800.0
	},
	"current_account": {
		"account_num": "009922",
		"amount": 120.0
	},
	"last_trxs": [80.0, 710.1, 1200.0, 290.3]
}

account_3 = {
	"user_id": "02231",
	"password": "pass555",
	"saving_bank": {
		"account_num": "009916",
		"amount": 1090.0
	},
	"current_account": {
		"account_num": "009926",
		"amount": 90.0
	},
	"last_trxs": [80.0, 2990.1, 110.0, 231.3, 970.3]
}

accounts = [account_1, account_2, account_3]
os.system('clear')

while True: 	
	print("\n\t@@@@@@@@@@@@@@@@@@@@@@@@")
	print("\t@@  Banco Digital LA  @@")
	print("\t@@@@@@@@@@@@@@@@@@@@@@@@")

	print("\nIngresar su ID")
	iuser_id = input(">> ")

	print("Ingresar su clave")
	ipassword = input(">> ")

	print("\nProcesando...")
	active_account = {}
	account_index = 0

	for account in accounts:
		if account['user_id'] == iuser_id and account['password'] == ipassword:
			active_account = account.copy()
			account_index = accounts.index(account)

	if len(active_account) != 0:

		while True:
			print("\nOperaciones disponibles")
			print("1) Acreditar en CA")
			print("2) Acreditar en CC")
			print("3) Consultar saldo en CA")
			print("4) Consultar saldo en CC")
			print("5) Consultar Trx")
			print("6) Salir")

			option = input(">> ")

			try:
				if int(option) < 1 or int(option) > 6:
					print("Debe seleccionar una opcion valida")
					continue

				if option == "1":
					print("Monto a acreditar en CA")
					credit = input("\t>> La$ ")

					active_account['saving_bank']['amount'] += float(credit)
					print("\n++ CA actualizada ++")

				if option == "2":
					print("Monto a acreditar en CC")
					credit = input("\t>> La$ ")

					active_account['current_account']['amount'] += float(credit)
					print("\n++ CC actualizada ++")

				if option == "3":
					print("\n++ Resumen de CA ++")
					print(f"Numero de cuenta: {active_account['saving_bank']['account_num']}")
					print(f"Saldo: La$ {active_account['saving_bank']['amount']}")

				if option == "4":
					print("\n++ Resumen de CC ++")
					print(f"Numero de cuenta: {active_account['current_account']['account_num']}")
					print(f"Saldo: La$ {active_account['current_account']['amount']}")

				if option == "5":
					print("Ultimas transacciones realizadas")
					for trx in active_account['last_trxs']:
						print(f"\tLa$ {trx}")
				
				if option == "6":
					os.system('clear')
					break

				print("---------------------")
			
			except ValueError:
				print("Debe ingresar numeros, no letras")
	else:
		print("\nPermiso denegado - Usuario invalido")

