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
        self.Autores = []
        
    def AnadirAutor(self,autor):
        self.Autores.append(autor)
        
#Mostramos el libro almacenado        
    def MostrarLibro(self):
        print("---------LIBRO-------")
        print("Titulo:",self.Titulo)
        print("ISBN:",self.Isbn)
        Autor.MostrarAutores(self)
        print("---------------------")
        
    def ObtenerTitulo(self):
        return self.Titulo

class Biblioteca:
#Almancenamos el listado de los libros
    def __init__(self):
        self.ListaLibros = []
#verificamos la cantidad de libros
    def NumeroLibros(self):
        return len(self.ListaLibros)
#Agregamos Libros
    def AnadirLibro(self,libro):
        self.ListaLibros = self.ListaLibros+[libro]
# Mostramos lo que ya esta guardado
    def MostrarBiblioteca(self):
        print("-------------LIBRO--------------------")
        for i in self.ListaLibros:
            i.MostrarLibro()
        print("--------------------------------------")
#creamos un menu
    def MostrarMenu(self):
        print("Menu\n 1.-Anadir Libros\n 2.-Mostrar Biblioteca\n 3.-Borrar Libro\n 4.-Numero de Libros\n 5.-Salir")
    
    def AgregarLibro(self):
        Titulo = input("Introduca el Titulo del Libro: ")
        Isbn = input("Introdusca el ISBN: ")
        AutorNombre = input("Introduce los nombres del Autor: ")
        AutorApellidos = input("Introduce los apellidos: ")
        Libro.AnadirAutor(AutorNombre,AutorApellidos)
        self.AnadirLibro(Titulo,Isbn)
        return self
#Mostrar biblioteca
    def MostrarBiblioteca(biblioteca):
        biblioteca.MostrarBiblioteca()
    
fin = False
biblioteca = Biblioteca()
while not fin:
    biblioteca.MostrarMenu()
    seleccion = int(input("Selecciona una opcion: "))
    if(seleccion == 1):
        biblioteca.AgregarLibro()
    elif(seleccion == 2):
        biblioteca.MostrarBiblioteca()
    elif(seleccion == 5):
        fin = True

print("Gracias por usar la biblioteca")
        

