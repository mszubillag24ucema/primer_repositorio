# Practico 2

# Ejercicio 1
bitcoin= "4.483.127"
ethereum = "308.416"
litecoin = "12.080"

print("-----------------")
print("Ejercicio 1")

print("La cotización de Bitcoin es:", bitcoin)
print("La cotización de Ethereum es:", ethereum)
print("La cotización de Litecoin es:", litecoin)

# Ejercicio 2
print("---------------")
print("Ejercicio 2")
print(f"La cotización de Bitcoin es: {bitcoin}")
print(f"La cotización de Ethereum es: {ethereum}")
print(f"La cotización de Litecoin es: {litecoin}")

# Ejercicio 3
print("---------------")
nombre = "Ernesto"
apellido = "Caldini"
mail = "Ecaldini@gmail.com"

# lower() Converts a string into lower case
# title() Converts the first character of each word to upper case

print("El nombre del usuario es:", nombre)
print(f"El apellido del usuario es: {apellido}")
print(f"El mail del usuario es: {mail}")

print("---------------")
x= nombre.lower()
y= apellido.lower()
z= mail.lower()
print("Los datos se almacenaran", x,y,z)

x= nombre.title()
y= apellido.title()
z= mail.title()
print("El usuario vera los datos", x, y, z)
print("---------------")

nombre= "ERNESTO   "
# rstrip() Returns a right trim version of the string, sin espacios

print(nombre.rstrip()) # No hace falta crear una nueva variable

# Ejercicio 4
print("---------------")

productos= 300
precio_dolar = 1500
cotizacion = 110
monto_a_importar= productos* precio_dolar* cotizacion
sellado=15000
comision = monto_a_importar* 0.3
total_a_importar = monto_a_importar + sellado + comision

print("El monto a importar es", monto_a_importar)
print("La comision a cobrar es", comision)
print("El total a cobrar es", total_a_importar)

comision_por_socio = comision/ 5 
print("La comision por socio sera", comision_por_socio)

print("-----------------")





