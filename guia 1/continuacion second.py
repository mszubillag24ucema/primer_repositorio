# Ejercicio 5
print("-------------------")

lista_nombres = ["ernest","martin andres","sofia","lucia","jose maria","abril"]

print("Los nombres de los Clientes son:")
# Si no pongo el titulo afuera me lo va a repetir adentro del loop del for

for nombre in lista_nombres:
      print(nombre.title())
"""
Para poner la primer letra de algo en mayusculas, el title se 
puede mandar adentro del print
"""

# Ejercicio 6
print("---------------")
lista_nombres_copy = lista_nombres[:]
lista_nombres_copy = lista_nombres_copy + ["martina", "josefina isabel", "tomas"]

print("La lista actualizada es:")
for nombre in lista_nombres_copy: 
        print(nombre.title())
lista_nombres_copy.pop()

final = []
for currency in lista_nombres_copy:
    final.append(currency.title())
print(final)
#en un loop, puedo ir agregando datos a la lista usando append
# Ejercicio 7
print("--------------------")
for numeros_naturales in range (0,102,2): 
    print(numeros_naturales)

# Ejercicio 8

print ("----------------")
lista1 = [117.12, 121.19, 128.37, 135.70, 139.47, 151.80, 157.95, 161.80,
166.20, 174.51, 179.68, 188.96, 200.89, 211.89, 225.99, 232.50,
249.12, 262.69, 177.67, 187.19, 193.81, 209.57, 216.73, 227.52,
239.24, 250.22, 256.04, 269.91, 282.93, 12.37, 92.17, 65.37,
73.26, 43.26, 78.26]

new_lista =[]
for lista in lista1:
    precio = round(lista * 1.07, 2)
    new_lista.append(precio)
    # ya me queda guardado en la lista
print(new_lista)
# Asi me imprime todo horizontal

"""
Cómo hacer para que me tire resultado con n de decimales dado
round(variable, q decimales)
"""

"""
"té", "café", "arroz", "harina 000", "lata de tomate", "jabón", "queso pategras", "leche", "levadura", "desodorante", "detergente", "agua con gas", "trapo de piso", "lavandina", "aceite de oliva", "vinagre", "mayonesa", "ketchup", "galletas de arroz"
ctl + H
ctl + a (seleccionar todo)
ctl + shipt + l (habilita multiple seleccion)
"""