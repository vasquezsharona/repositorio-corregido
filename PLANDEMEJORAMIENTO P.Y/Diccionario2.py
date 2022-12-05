#Escribir un programa que guarde en una variable el diccionario 
#{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y 
#muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

monedas = {'Euro':'€', 'Dolar':'$', 'Yen':'¥'}

def buscarMoneda():
    moneda = input("Introduce una divisa: ")
    if moneda in monedas.values():
        print(moneda,'Si está.')
        exit()
    else:
        print("La moneda no está.")

while True:

    buscarMoneda()