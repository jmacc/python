# Clase Autor

class Autor:
    def __init__(self, Nombre, Apellido):
        self.Nombre = Nombre
        self.Apellido = Apellido

    def MostrarAutor(self):
        print("Autor: ", self.Nombre, " ", self.Apellido)


class Libro:
    def __init__(self, Titulo, ISBN):
        self.Titulo = Titulo
        self.ISBN = ISBN

    def NuevoAutor(self, Autor):
        self.Autor = Autor

    def MostrarLibro(self):
        print(" ---------- LIBRO ---------- ")
        print("Titulo: ", self.Titulo)
        print("ISBN: ", self.ISBN)
        self.Autor.MostrarAutor()
        print(" --------------------------- ")

    def ObtenerTitulo(self):
        return self.Titulo


class Biblioteca:
    def __init__(self):
        self.ListaLibros = []

    def NumeroLibros(self):
        return len(self.ListaLibros)

    def MostrarBiblioteca(self):
        print("-----------------------")
        for item in self.ListaLibros:
            item.MostrarLibro()
        print("-----------------------")

    def BorrarLibro(self, titulo):
        encontrado = False
        posicionborrar = -1
        for item in self.ListaLibros:
            posicionar += 1
            if item.ObtenerTitulo() == titulo:
                encontrar = True
                break
        if encontrado:
            del self.ListaLibro[posicionborrar]
            print("Libro Borrado Correctamente")
        else:
            print("Libro no encontrado")

    # Menu
    def MostrarMenu():
        print("Menu\n 1 .- Anadir Libros\n 2.-Mostrar Biblioteca\n 3.-Borrar Libro\n 4.-Numero de Libros\n 5.-Salir")

    def NuevoLibroBiblioteca(biblioteca):

        # Pedimos datos
        Titulo = print(input("Ingresa un titulo"))
        ISBN = print(input("Ingresar el ISBN"))
        AutorNombre = print(input("Ingresar el Nombre del Autor"))
        AutorApellidos = print(input("Ingresar Apellido del Autor"))

        # Asignacion

Inicio = Biblioteca()
Inicio.MostrarMenu
