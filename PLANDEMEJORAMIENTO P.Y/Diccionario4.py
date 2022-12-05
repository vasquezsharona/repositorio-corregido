#Escribe un programa que lea una cadena y devuelva un diccionario con la 
#cantidad de apariciones de cada carácter en la cadena. 

dicc = {}

palabra = input("Digite una palabra: ")

for letras in palabra:
	if letras in dicc:
		dicc[letras] += 1
	else:
		dicc[letras] = 1

print(dicc)