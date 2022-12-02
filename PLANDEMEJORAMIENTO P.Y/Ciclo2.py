#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

edad = int(input('Digite su edad: '))

for años in range(1,edad,1):#el último número es la forma en que se va a contar.
    print(años)