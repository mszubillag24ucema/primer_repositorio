# Ejercicio 6
customer_payments = ['23423', '58092', '75230', '72879', '82231', '35465', '30943', '12772']
cards_trx = [
    {'user_id': '35465', 'total_amount': 30000, 'payment_method': 'credit card',
     'total_installments': 12, 'current_installment': 7},
    {'user_id': '23423', 'total_amount': 19099, 'payment_method':'credit card', 'total_installments': 12, 'current_installment': 3},
    {'user_id': '82312', 'total_amount': 15500, 'payment_method': 'credit card', 'total_installments': 12, 'current_installment':
    4},{'user_id': '29332', 'total_amount': 90200, 'payment_method':
    'credit card', 'total_installments': 6, 'current_installment':
    4}, {'user_id': '82231', 'total_amount': 29000, 'payment_method':
    'credit card', 'total_installments': 12, 'current_installment':
    9}, {'user_id': '76289', 'total_amount': 42300, 'payment_method':
    'credit card', 'total_installments': 12, 'current_installment':
    11}, {'user_id': '58092', 'total_amount': 18900, 'payment_method':
    'credit card', 'total_installments': 6, 'current_installment':
    1}, {'user_id': '30943', 'total_amount': 13520, 'payment_method':
    'debit card'}, {'user_id': '75230', 'total_amount': 67000, 'payment_method':
    'credit card', 'total_installments': 6, 'current_installment':
    4},{'user_id': '20582', 'total_amount': 21500, 'payment_method':
    'credit card', 'total_installments': 12, 'current_installment':
    6},  {'user_id': '10943', 'total_amount': 5200, 'payment_method':
    'debit card'}, {'user_id': '29002', 'total_amount': 9000, 'payment_method':
    'credit card', 'total_installments': 12, 'current_installment':
    11}, {'user_id': '92389', 'total_amount': 39200, 'payment_method':
    'debit card'}, {'user_id': '12772', 'total_amount': 65700, 'payment_method':
    'credit card', 'total_installments': 12, 'current_installment':
    10}, {'user_id': '72879', 'total_amount': 7300, 'payment_method':
    'credit card', 'total_installments': 6, 'current_installment':
    5}, {'user_id': '83489', 'total_amount': 44000, 'payment_method':
    'debit card'}]

remaining_installment = 0
users_id = []
print("---------------------")
print(f"Se actualizaron los siguientes current_installments:")
for customer in customer_payments:
    for client in cards_trx:
        if customer == client["user_id"] and client["payment_method"] != "debit card":
            client["current_installment"] = client["current_installment"] + 1
            print(f"{customer}  current_installment {client['current_installment']}")

print("---------------------")

for customer in customer_payments:
    for client in cards_trx:
        if customer == client["user_id"] and client["payment_method"] != "debit card":
            remaining_installment = client["total_installments"] - client["current_installment"]
            print(f"Al cliente {customer} le restan pagar {remaining_installment} cuotas")
        if remaining_installment == 0 or client["payment_method"] == "debit card":
            users_id.append(client["user_id"])

print("---------------------")
print(f"Los clientes que cumplieron con su pago son: \n {set(users_id)}")
