#Library - Biblioteca

#Clase autor
class Autor():
    def __init__(nom,apell):
        nombre = nom
        apellido = apell
        print('El autor es: '(nombre," ",apellido))
        
#Clase Libro
class Libro():
    def __init__(self,titulo,isbn):
        self.titulo = titulo
        self.isbn = isbn
        
    def anadirAutor(self,autor):
        self.autor = autor
        
print("Ingresamos datos")
nombre1 = "Jose"
apellido1 = "Castillo"
#isbn = "ajd837jsjw"

Autor1 = Autor(nombre1,apellido1)
print(str(Autor1))

