#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

while True:

    numero = int(input("Ingrese un número: "))

    if numero % 2 == 0:
        print(numero," es par.")
    else:
        print(numero," es impar")