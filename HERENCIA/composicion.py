class  Aprendiz : # se crea una clase nombrada (Aprendiz)
    def  __init__ ( self , nombre ): # se crea un constructor con un parámetro nombrado (nombre)
        uno mismo __nombre = nombre  # se le asigna el parametro al atributo
        uno mismo __cursos = [] # se crea una lista vacia al atributo

    def  agregarCurso ( self , titulo ): # se crea un metodo con el parametro (titulo)
        uno mismo __cursos . append ( título ) # se le agrega el parámetro al atributo

    def  getCursos ( self ): # se crea un método sin parámetro
        devolverse  a uno mismo . __cursos  # devuelve el valor del atributo instanciado

class  Curso : # se crea una clase nombrada (curso)
    def  __init__ ( self , titulo ): # se crea un constructor con el parametro de titulo
        uno mismo __titulo = titulo  # se le asigna el parametro al atributo

    def  getTitulo ( self ): # se crea un metodo sin parametros
        devolverse  a uno mismo . __titulo  # devuelve el valor del atributo instanciado

a = Aprendiz ( 'Martha' ) # se crea un objeto de la clase aprendiz y se envia como parametro ('martha')
c1 = Curso ( 'Python Intermedio' ) # se crea un objeto de la clase curso que instancia como parametro ('Python Intermedio')
c2 = Curso ( 'Python Basico' ) # se crea otro objeto que trae la clase curso, instanciando como parametro ('Python Basico')
c3 = Curso ( 'Introduccion a Java' ) # se crea otro objeto que trae la clase curso, instanciando como parametro ('Introduccion a Java')

un . agregarCurso ( c1 ) # llamamos el objeto creado invocando el metodo, instanciandole como parametro (c1)
un . agregarCurso ( c2 ) # llamamos el objeto creado invocando el metodo, instanciandole como parametro (c2)
un . agregarCurso ( c3 ) # llamamos el objeto creado invocando el metodo, instanciandole como parametro (c3)

print ( a . getCursos ()) # Que imprima, el objeto invocando el metodo (getCursos)


para  el cursor  en  un . getCursos (): # se crea un bucle for para que recorra la clase curso en instancia con el objeto (a) invocado del metodo (getCursos)
    print ( curso . getTitulo ()) # Que imprima, la clase curso invocado del metodo gettitulo
