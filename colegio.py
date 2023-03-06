
class USUARIO:
    def __init__(self,nombre):
        self.nombre=nombre
    def getnombre(self):
        return 'Nombre del estudiante es: ', self.nombre 
        
        
class registro:
    
    def __init__(self,id,edad, numerocontacto, nombredeusuario, contraseña):
        self.id=id
        self.edad=edad
        self.numerocontacto=numerocontacto
        self.nombredeusuario=nombredeusuario
        self.contraseña=contraseña
        self.dato=[]
    
    def agregarid(self,identi):
        ide=USUARIO(identi)
        self.dato.append(ide)
    
