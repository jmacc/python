#Creamos los Libros
class Autor:
    def __init__(self,nombre,apellido):
        self.Nombre = nombre
        self.Apellido = apellido
    
    def MostrarAutores(self):
        print("Autor: ",self.Nombre, " ",self.Apellido)

class Libro:
    def __init__(self,titulo, isbn):
        self.Titulo = titulo
        self.Isbn = isbn
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
    def  CantidadLibros(self):
        return len(self.ListaLibros)
#Agregamos Libros
    def AnadirLibro(self,libro):
        self.ListaLibros = self.ListaLibros+[libro]
# Mostramos lo que ya esta guardado
    def MostrarlibrosBiblioteca(self):
        print("-------------LIBRO--------------------")
        for i in self.ListaLibros:
            i.MostrarLibro()
        print("--------------------------------------")
#Eliminados el Libro elegido
    def BorrarLibro(self,titulo):
        encontrado = False
        posicionborrar = -1
        for item in self.ListaLibros:
            posicionborrar +=1
            if item.ObtenerTitulo() == titulo:
                encontrado = True
                break
            if encontrado:
                del self.ListaLibros[posicionborrar]
                print("Libro BORRADO correctamente")
            else:
                print("Libro no Encontrado")
#creamos un menu
    def MostrarMenu(self):
        print("Menu\n 1.-Anadir Libros\n 2.-Mostrar Biblioteca\n 3.-Borrar Libro\n 4.-Numero de Libros\n 5.-Salir")
    
    def AgregarLibro(self):
        Titulo = input("Introduca el Titulo del Libro: ")
        Isbn = input("Introdusca el ISBN: ")
        libro = Libro(Titulo,Isbn)
        AutorNombre = input("Introduce los nombres del Autor: ")
        AutorApellidos = input("Introduce los apellidos: ")
        autor = Autor(AutorNombre,AutorApellidos)
        libro.AnadirAutor(autor)
        biblioteca.AnadirLibro(libro)
        return biblioteca
        
#Mostrar biblioteca
    def MostrarBiblioteca(biblioteca):
        biblioteca.MostrarlibrosBiblioteca()
    
    def BorrarLibro(biblioteca):
        titulo = input("Introduce el titulo del libro: ")
        biblioteca.BorrarLibro(titulo)
        
    def NumeroLibros(biblioteca):
        print("El numero de libros es: ", biblioteca.CantidadLibros())
    
fin = False
biblioteca = Biblioteca()
while not fin:
    biblioteca.MostrarMenu()
    seleccion = int(input("Selecciona una opcion: "))
    if(seleccion == 1):
        biblioteca.AgregarLibro()
    elif(seleccion == 2):
        biblioteca.MostrarBiblioteca()
    elif(seleccion == 3):
        biblioteca.BorrarLibro()
    elif(seleccion == 4):
        biblioteca.NumeroLibros()
    elif(seleccion == 5):
        fin = True

print("Gracias por usar la biblioteca")
        

