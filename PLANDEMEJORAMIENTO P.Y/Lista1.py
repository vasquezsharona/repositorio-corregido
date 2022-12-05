#Escribir un programa que almacene las asignaturas que ingrese un usuario
#(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

materias = []
materia = 0

while materia != '':
    materia = input('Ingrese una materia: ')
    if materia == '':
        break
    materias.append(materia)
    print(materias)

#https://aprendeconalf.es/docencia/python/ejercicios/listas-tuplas/