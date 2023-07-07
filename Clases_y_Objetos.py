#Clases u Objetos
"""
class Galleta:
    chocolate = False
    
    def saludar(soy_el_objeto):
        print("Hola soy una sabrosa galleta")
        print(soy_el_objeto)
        
#print(Galleta) # Imprimre que es una clase
redonda = Galleta()#instancia de la clase y se crea el objeto
#print(redonda) #imprime la ubicacion del objeto
#print(redonda.chocolate) #accedo al valor actual de galleta
redonda.saludar()#metodo de instancia
print(redonda.saludar) #metdodo de galleta.saludar del objeto galleta
#Galleta.saludar()#metodo de la clase
print(Galleta.saludar)#funcion galleta saludar
##############################################

class Person:
    def __init__ (self,n,e):
        self.name = n
        self.age = e
    
    def view_name(self):
        print("Tu nombre es: ",self.name)
    def vie_age(self):
        print("Tu edad es: ",self.age)
        
Person1 = Person("jose",14)
Person1.view_name()
Person1.vie_age()
##############################################

class Student:
    
    def __init__(self,name,subjects):
        self.set_name(name)
        if not isinstance(subjects,list):
            raise TypeError("subject must be a list")
        self.subjects = subjects
        
    def set_name(self,name):
        if not isinstance(name,str):
            raise TypeError("Name must be a string")
        self._name = name
        
    def get_name(self):
        return self._name
    
student = Student("Pablo", [5, 14, 3])
student.print_info()
##############################################
"""

class Pelicula:
     # Constructor de clase
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.lanzamiento = lanzamiento
        self.duracion = duracion
        print("Se ha creado la pelicula: ,",self.titulo)
        
    def __str__(self): #la forma en que se visualizan los datos
        return '{} ({})'.format(self.titulo,self.lanzamiento)
    
class Catalogo:
    Peliculas = [] # Esta lista contendrá objetos de la clase Pelicula
        
    def __init__(self,Peliculas=[]):
            self.Peliculas = Peliculas
            
    def agregar(self, p):# p será un objeto Pelicula
            self.Peliculas.append(p)
            
    def mostrar(self):
        for p in self.Peliculas:
            print(p) # Print toma por defecto str(p)
                
pep = Pelicula("El padrino",150,1859)
cat = Catalogo([pep]) # Añado una lista con una película desde el principio
cat.mostrar()