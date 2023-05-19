#Creamos los Libros
class Autor:
    def __init__(self,Nombre,Apellido):
        self.Nombre = Nombre
        self.Apellido = Apellido
        
    def MostrarAutores(self):
        print("Autor: ",self.Nombre, " ",self.Apellido)

class Libro:
    def __init__(self,Titulo, ISBN):
        self.Titulo = Titulo
        self.Isbn = ISBN
        
    def NuevoAutor(self,Autor):
        self.Autor = Autor

class Biblioteca:
#agregamos los libros
    def __init__(self):
        self.ListaLibros = []
#verificamos la cantidad de libros
    def NumeroLibros(self):
        return len(self.ListaLibros)
#creamos un menu
    def MostrarMenu(self):
        print("Menu\n 1.-Anadir Libros\n 2.-Mostrar Biblioteca\n 3.-Borrar Libro\n 4.-Numero de Libros\n 5.-Salir")
    
    def AgregarLibro(biblioteca):
        Titulo = input("Introduca el Titulo del Libro: ")
        Isbn = input("Introdusca el ISBN: ")
        AutorNombre = input("Introduce los nombres del Autor: ")
        AutorApellidos = input("Introduce los apellidos: ")
        #Complementamos Autor
        autor = Autor(AutorNombre,AutorApellidos)
        #Complementamos Libros
        libro = Libro(Titulo,Isbn)
        #Agregamos Autor
        libro.NuevoAutor(autor)
        #Agregamos Libros
        biblioteca.AgregarLibro(libro)
        return biblioteca
    
fin = False
biblioteca = Biblioteca()
while not fin:
    biblioteca.MostrarMenu()
    seleccion = int(input("Selecciona una opcion: "))
    if(seleccion == 1):
        biblioteca.AgregarLibro(biblioteca)
        

