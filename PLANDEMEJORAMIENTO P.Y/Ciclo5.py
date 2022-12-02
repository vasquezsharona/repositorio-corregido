#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

contraseña = 'sena'

contraUsuario = input('¿Cuál es la contraseña?')

while contraUsuario != contraseña:#!= diferente de:
    contraUsuario = input('No es, digite otra contraseña?')
print('Acertó')