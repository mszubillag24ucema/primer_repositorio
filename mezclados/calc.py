# numero1 = int (input ("Escriba el primero numero:"))
# numero2 = int (input("Escriba el segundo numero:"))
import sys
# Para navegar solo en la terminal
# Run ejecuta comandos desde la terminal
print(sys.argv)
# convierte los parametros de entrada en una lista

lista = sys.argv
numero1 = int(lista[1])
numero2 = int(lista[2])
# operacion = lista[3]
print(f" La suma de los numeros es: {numero1} + {numero2}")

# operacion = input(f"Qué operacion:")
"""
if(operacion == "+"):
    print (numero1 + numero2)
elif (operacion == "-"):
    print(numero1 - numero2)
elif (operacion == "*"):
    print(numero1 * numero2)
else: 
    print( numero1 / numero2)
"""

