#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

numero = int(input("Introduce un número positivo: "))

for regresiva in range(numero, 0 - 1, -1):
    print(regresiva, end=", ")