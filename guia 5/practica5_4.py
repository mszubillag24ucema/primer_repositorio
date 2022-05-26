# exercise 3
curso = [
    {'ID': 'AM322', 'notas': (7, 4, 8, 9)},
    {'ID': 'JL323', 'notas': (5, 5, 5, 5)},
    {'ID': 'OP324', 'notas': (4, 4, 3)},
]


'''
Definir una función que recorra la lista de notas finales y utilizando “print()”
mostrar de forma prolija.
'''

lista_notas = []


def calc_notas():
    for curs in curso:
        note = {}
        q_notas = len(curs['notas'])
        suma = sum(curs['notas'])
        nota = round(suma / q_notas, 3)
        ids = curs['ID']
        note['ID'] = ids
        note['nota'] = nota
        lista_notas.append(note)


calc_notas()
print(f' {lista_notas} ')




