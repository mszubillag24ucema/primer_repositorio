# definimos una clase/objeto
class Ballena:
    def __init__(self, nombre, edad, sexo, peso, mamifero):
        # cada uno de estos es un atributo
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.mamifero = mamifero
        # hasta aca es el constructor

    # vamos a definir funciones
    # las funciones dentro de objetos se llaman METODOS
    def nadar(self):
        return f"{self.nombre} esta nadando..."

    def saltar(self):
        return f"{self.nombre} va a saltar la escollera..."

    def alimentarse(self):
        return f"{self.nombre} esta alimentandose..."

    def descansar(self):
        return f"{self.nombre} zzzzzzzzZZZZ..."

    def estado(self):
        return f"Estado de la ballena:" \
               f"\n\tNombre: {self.nombre}" \
               f"\n\tEdad: {self.edad}" \
               f"\n\tSexo: {self.sexo}" \
               f"\n\tPeso: {self.peso}" \
               f"\n\tEs mamifero: {'SI' if self.mamifero else 'NO'}"


# las siguientes son variables que dentro tienen un objeto
# representaciones iguales pero objetos diferentes por existir en diferentes espacios
willy = Ballena('Willy', 9, 'M', 2000, True)
willy_clone = Ballena('Willy', 9, 'M', 2000, True)
# cada uno de los aneriores es un atributo de willy
print(f'Mi ballena es: {willy.nombre}')
# ese print no imprime nada porque solo lo definimos, tengo que usar DOTS
print(willy.nadar())
print(f'{willy.estado()}')
