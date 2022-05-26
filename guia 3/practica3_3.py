"""
# Variables (string, boolean, number (int o float)
# Lista ['string', boolean, 1, 2, [...], ...] --> index 0 - N --> len(lista)
# Diccionarios {k: v}
# Tupla ('rodri'), Conjunto {1, 2, 3, 4}

# funciones del lenguaje: len(), print(), int("1"), float("1.2")


# RUNNING -> TOP -> BOTTOM

botellas = ['vidrio', {'botella': 'plastico'}, ['acero']]

for botella in botellas:
    print(f"Tipo de dato: {type(botella)}")
    print(f"Valor: {botella}")
"""

# Ejercicio 5
ee_uu = {"pais": "EE.UU", "cities": ["New York", " Boston"], "currency": "dolar", "language": "inglés"}
costa_rica = {"pais": "Costa Rica", "cities": ["San José", "Santa Teresa"], "currency": "CRC", "language": "español"}
mexico = {"pais": "Mexico", "cities": ["DF", "Cancun"], "currency": "MX", "language":  "español"}
canada = {"pais": "Canada", "cities": ["Toronto", "Montreal"], "currency": "CAD", "language": "inglés"}
alemania = {"pais": "Alemania", "cities": ["Berlín", " Munich"], "currency": "EUR", "language": "alemán"}
francia = {"pais": "Francia", "cities": ["París", "Lyon"], "currency": "EUR", "language": "francés"}
suiza = {"pais": "Suiza", "cities": ["Geneva",  "Bern"], "currency": "CHF", "language": "alemán"}
esp = {"pais": "España", "cities": ["Madrid",  "Mallorca"], "currency": "EUR", "language": "español"}
italia = {"pais": "Italia", "cities": ["Roma", "Nápoles"], "currency": "EUR", "language": "italiano"}

countries = [ee_uu, costa_rica, mexico, canada, alemania, francia, suiza, esp, italia]

suecia_ok = False
df_exist = False
vist_cities = []

for country in countries:
    if country["pais"] == 'Suecia':
        suecia_ok = True

    for city in country['cities']:
        vist_cities.append(city)
        if city == 'DF':
            print(f"La ciudad DF existe en destinos a visitar - {city}")

print(f"Existe Suecia: {suecia_ok}")
print(f"Todas las ciudades a visitar: \n {vist_cities}")

# Ejercicio 7 | Random

numbers = []

for number in range(101):

    if number == 0:
        print(f"NUMBER TO AVOID: {number}")
        continue

    number_dict = {}
    number_dict['number'] = number

    if number % 2 == 0:
        number_dict['type'] = "par"
    else:
        number_dict['type'] = "impar"

    numbers.append(number_dict)

print(numbers)










