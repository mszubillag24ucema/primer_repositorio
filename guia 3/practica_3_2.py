# Ejercicio 3

usuarios = {"nombre": "Rodri", "apellido": "Gonzalez",
           "dni": "34506899", "rol": "CFO", "sucursal": "001"}
for key, value in usuarios.items():
  print(f"{key.upper()}-{value}")


# Ejercicio4
print("------------------")
dict = {'anonimo1': '6', 'anonimo2': '9', 'anonimo3': '5', 'anonimo4':
    'x', 'anonimo5': 'x', 'anonimo6': '8', 'anonimo7': '3',
    'anonimo8': '10', 'anonimo9': '4', 'anonimo10': '5', 'anonimo11':
    'x', 'anonimo12': '2', 'anonimo13': '7', 'anonimo14': '5',
    'anonimo15': '2', 'anonimo16': '8', 'anonimo17': '10'}

dict1 = dict.copy()
y = 0
for value in dict.values():
    if value == "x":
        y += 1
print(f"No votaron {y} personas")

for key, value in dict.items():
    if dict.get(key) == "x":
        dict1.pop(key)
# No puedo ir eliminando elemento de las lista que corro al mismo tiempo, lo haso desde una copy
print(dict1)
print(f"La cantidad que votaron fue {len(dict1)}")
suma = 0
for value in dict1.values():
    suma = suma + int(value)

aceptacion = suma / 100
print(f"La aceptacion fue de {aceptacion*100}%")

puntuacion = []
for value in dict1.values():
    puntuacion.append(int(value))
print(sorted(set(puntuacion)))

