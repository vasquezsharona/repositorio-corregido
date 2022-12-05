'''Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista 
y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una 
de las asignaturas de la lista.'''

materias = []
materia = 0

while True:
    materia = input('Ingrese una materia: ')
    if materia == '':
        break
    materias.append(materia)
    print(materias)

for materia in materias:
    print("Yo estudio " + materia)