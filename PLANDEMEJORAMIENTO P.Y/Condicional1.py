#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

num1 = float(input('numero 1: '))
num2 = float(input('numero 2: '))

if num2 == 0:
    print('Error')
else:
    print(num1 / num2)