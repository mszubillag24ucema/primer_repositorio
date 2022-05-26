# Ejercicio 9
encuesta= [True, False, True, True, True, False, True, False, True, True,
True, False, False, True, True, True, True, False, True, True,
True, False, True, True, False, True, True, False, True, False,
True, True, True, False, True, True, True, False, True, False,
True, True, True, False, False, True, True, True, True, False,
True, True, True, False, True, True, False, True, True, False,
True, False, True, True]

si= 0
no= 0
cantidad_encuestados = len(encuesta)

for currency in encuesta:
    if currency: #poner currency ==True seria sobre nombrarlo
        si+=1
    else:
        no+=1

promedio_si = (si/cantidad_encuestados)*100
promedio_no = (no/cantidad_encuestados)*100
print(f"Le gustó a {si} personas. El {promedio_si}% de los encuestados")
print(f"No le gustó a {no} personas. El {promedio_no}% de los encuestados.")

if promedio_si > 65:
    print("Producto exitoso")
else:
    print("Aún hay que mejorar el producto")

#Ejercicio 10
lista = ["té", "café", "arroz", "harina 000", "lata de tomate", "jabón", "queso pategras", "leche", "levadura", "desodorante", "detergente", "agua con gas", "trapo de piso", "lavandina", "aceite de oliva", "vinagre", "mayonesa", "ketchup", "galletas de arroz"]

producto = input("Ingrese el producto buscado:")
if producto in lista:
    print(f"producto en existencia: {producto}")
else:
    print(f"El proveedor no cuenta con el producto: {producto}")

#Ejercicio 11
usuarios = ["marmeant", "gruntmar", "tokcie", "ciebank", "mueslicie", "sanero", "robedrock", "admin", "derivero","posloth", "claypo", "locustpo", "mostter" ]

acceso = input("Ingrese su usuario:")
denegado = "tokcie"

if acceso == denegado:
    print(f"User {acceso} access denied")
elif acceso in lista:
     print(f"Bienvenido estimado {acceso.title()}, le deseamos un buen día")
else:
    print(f"Bienvenido Administrador, en que lo podemos ayudar")

