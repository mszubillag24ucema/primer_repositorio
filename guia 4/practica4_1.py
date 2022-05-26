print("\n----------------------")

# cualquier dato que escribamos en input va a entrar como string
# si no quiero que el dato de entrada sea string, uso int o float
# type(): me devuelve que tipo de dato es una variable
'''
message = " "
active = True
# active es mi flag, el while se ejecuta hasta que sea False
while active:
    message = input("Enter your name:")
    if message == "quit":
        active = False
    else:
        print(message)
'''
# vamos a necesitar un break por cada for que usemos
'''
try:
    what i want to execute
else el tipo de error que puede aparecer:
    ejecucion de lo que quiero hacer
'''
# Ejercicio 1 y 2
print("\n**************************")
print ("Welcome to Disney World")
print("\n**************************")

print("Buy a ticket, please enter your age:")

while True:
    age = input(">> ")
    if age == "quit":
        break
# try and else son para el punto 2, sobre solución de errores
    try:
        if int(age) < 5:
            print("The Ticket is free")
        elif int(age) >= 5 and int(age) < 9:
            print("Ticket price USD 15")
        elif int(age) >= 9 and int(age) < 14:
            print("Ticket price USD 23")
        elif int(age) >= 14 and int(age) < 100:
            print("Ticket price USD 35")
        else:
            print("You're awsome!! Free ticket :)")
    except ValueError:
        print("You can't enter letters. Please enter numbers")

print("Finish Program")