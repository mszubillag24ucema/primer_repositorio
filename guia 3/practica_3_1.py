# Ejercicio1
usuario = {"nombre": "Rodri", "apellido": "Gonzalez",
           "dni": "34506899", "rol": "CFO", "sucursal": "001"}

# values() me imprime los valores, no los key
# keys() imprime solo los keys como los tengo escritos
# items() devuelve una tupla de clave valor

"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""
print("------------------")
for key, value in usuario.items():
    # como tengo un par, puedo mandar dos var en el for
    print(f"{key.title()}: {value}")
    # clean code

# Ejercicio2
print("------------------")
"""
Lita “[]”
Tupla “()”
Conjunto “{}”
Diccionario “{k:v}”
"""
animals_list =["cat", "dog", "butterfly"]
animals_tuple = ("cat", "dog", "butterfly")
animals_set = {"cat", "dog", "butterfly"}
animals_dict = {"cat": "cat", "dog": "dog", "butterfly": "butterfly"}
python_animal = "python"

print("------------------")
print(animals_list)
print(animals_tuple)
print(animals_set)
print(animals_dict)

animals_list.append(python_animal)
animals_set.add(python_animal)
# in tuple and dict we cannot add elements
# set no acepta datos duplicados
print(animals_list)
print(animals_set)



