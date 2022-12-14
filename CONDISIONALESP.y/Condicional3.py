#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
#pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
#por el usuario coincide con la guardada en la variable.

clave = "nomeacuerdo"

while True:

    palabra = input("Introduce la clave: ")

    if clave == palabra:
        print("La clave es correcta.")
        break
    else:
        print("La clave es incorrecta.")