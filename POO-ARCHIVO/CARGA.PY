from  Vehiculo  import  *  # se importa la clase con todos sus atributos
class  Carga ( Vehiculo ): # se crea la clase carga y tendra herencia con la clase vehiculo
    def  __init__ ( self , placa , conductor , capacidad , ejes ): # se crea un constructor con parametros asignados
        vehiculo _ __init__ ( self , placa , conductor ) # se instancia el constructor con sus parámetros de la clase padre
        uno mismo __capacidad = capacidad  # atributo va aser igual al parametro
        uno mismo __ejes = ejes  #el atributo va a ser igual al parametro  
    def  getPlaca ( self ): # se crea un metodo
        devolverse  a uno mismo . __placa  #ddevuelve el valor del atributo
    def  getCapacidad ( self ): # se crea un metodo
        devolverse  a uno mismo . __capacidad  # devuelve el valor del atributo
    def  getConductor ( self ): # se crea un metodo
        devolverse  a uno mismo . __conductor  #devuelve el valor del atributo
    def  getEjes ( self ): # se crea un metodo
        devolverse  a uno mismo . __ejes  #devuelve el valor del atributo
