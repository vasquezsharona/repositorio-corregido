#Cree un diccionario vacío y llenelo con los estudiantes que considere
#que van a aprobar el plan de mejoramiento.

dicc = {'estudiantes':{}} 

while True:

    nombre = input('Ingrese el nombre del estudiante: ')
    if nombre == '':
        break
    aprobar = input("Escriba 'aprueba' o 'reprueba' según su consideración: ")

    dicc['estudiantes'][nombre] = aprobar

    print(dicc)