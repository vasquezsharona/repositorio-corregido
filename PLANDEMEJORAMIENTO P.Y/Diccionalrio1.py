#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono 
#y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años,
#vive en <dirección> y su número de teléfono es <teléfono>.

nombre = input('Nombre: ')
edad = input('Edad: ')
direccion = input('Dirección: ')
telefono = input('Teléfono: ')

usuario = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}

print(usuario['nombre'], 'tiene', usuario['edad'], 'su dirección es', usuario['direccion'], 'y su teléfono es', usuario['telefono'])

#https://www.mclibre.org/consultar/python/ejercicios/ej-listas-1.html