#funicones para hacer sentencias independientesimport sqlite3 # queda instanciado coneccion y el cursor 
#f =plantilla literal
# cuando es relativa  solo 1 \

with sqlite3.connect('C:\\Vasquez\\db\\conpython.db')as con: # queda instanciado coneccion y el cursor with crear flujo de archivos
    micursor=con.cursor()#instanciamos un objeto
    sentencia='select* id,nombre,apellido from alumno WHERE ID>=400;'
    print(micursor.execute(sentencia).fetchall()) #ejecuta la sentencia de arriba 



def miselect(conexion,campo,operador,dato): #  funcion que tiene 5 parametros 
   micursor=conexion.cursor()#instanciamos un objeto 
   sentencia='select*from{tabla} WHERE {campo}{operador}{dato}}'#codigo sql con el que se ingresa a la bd  
   print(sentencia) # imprime la sentenia
   print(micursor.execute(sentencia).fetchall())



miselect ( estafa , 'alumno' , 'correo electrónico' , '=' , 'dbrabon2@irs.gov' )
