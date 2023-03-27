import sqlite3 # queda instanciado coneccion y el cursor 
with sqlite3.connect('C:\\Vasquez\\db\\conpython.db')as con: # queda instanciado coneccion y el cursor 
    micursor=con.cursor()
    sentencia='select* nombre,apellido from alumno;'
    print(micursor.execute(sentencia).fetchall()) #ejecuta la sentencia de arriba 
