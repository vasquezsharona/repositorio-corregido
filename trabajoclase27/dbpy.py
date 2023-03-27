#codigo suelto conectando sqlite con py


import sqlite3 # importa
con=sqlite3.connect('C:\\Vasquez\\db\\conpython.db') # sqlite3  objeto # instanciacion 
print(type(con))

# cursor 

micursor=con.cursor
print(type(micursor))
sentencia='select * from alumno;'
micursor .execute(sentencia)
print(micursor.fetchall()) #fetchall realiza una lista de tuplas 

micursor .execute(sentencia)
