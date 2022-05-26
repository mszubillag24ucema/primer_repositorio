estudiantes = [37128693, 38346828, 48577851, 23923908, 23747794, 46033685, 28372488, 33143443,
38122921, 38915457, 24807285, 35759559, 21061055, 33613272, 24082600, 26477319,
46655903, 46988530, 25145603, 35368988, 25393784, 21295674, 48348316, 31247247,
28498292, 37538741, 21332845, 27557703, 24435687, 38794110, 44518399, 34178717,
45788239, 36998322, 32098132, 22185788, 25030083, 21256524, 34592517, 41755997,
37570846, 30401721, 34832996, 47330519, 34380715, 42724546, 26615771, 23171192,
42223891, 40210778, 33530381, 20478110, 20753240, 28187999, 27785500, 37236996,
22981717, 27744330, 44855039, 36552090, 36824210, 39684157, 26469844, 45037525,
25916934, 41595563, 23571241, 30552911, 40100736, 36047292, 46818813, 36680587,
36107300, 41367347]

notas = [15, 19, 19, 9, 6, 12, 20, 3, 1, 15, 10, 16, 3, 25, 18, 13, 24, 30, 7, 28, 20, 25, 28, 10, 2, 1,
18, 20, 3, 3, 19, 12, 11, 8, 24, 27, 15, 15, 19, 0, 27, 8, 29, 5, 1, 12, 8, 17, 19, 0, 0, 18, 15,
23, 22, 2, 24, 6, 10, 28, 18, 3, 15, 6, 26, 0, 21, 14, 24, 13, 10, 17, 16, 2]

#Buscar mi nota

print("---------------")
print("Las notas de los estudiantes son:")

n = 0
while n < len(estudiantes):
    for estudiante in estudiantes:
     nota = notas[n]
     print(estudiante, "    ", nota)
     n += 1

#Sepraración por nivel

avanzado = 0
intermedio_alto = 0
intermedio_bajo = 0
basico = 0
por_debajo = 0

print("---------------")
for nota in notas:
    if (nota >= 25) and (nota <= 30):
        avanzado += 1
    elif (nota >= 20) and (nota <= 24):
        intermedio_alto += 1
    elif (nota >= 16) and (nota <= 19):
        intermedio_bajo += 1
    elif (nota >= 10) and (nota >= 15):
        basico += 1
    else:
        por_debajo += 1

print(f"El total de exámenes es: {len(estudiantes)}")
print("---------------")
print(f"Siendo: \n Avanzados: {avanzado} \n Intermedios altos: {intermedio_alto} \n Intermedios bajos: "
      f"{intermedio_bajo} \n Básicos: {basico} \n Por debajo del básico: {por_debajo} ")










