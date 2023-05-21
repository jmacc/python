#Métodos en Python: instancia, clase y estáticos

class Clase:
    def metodo(self):
        return "Metodo Normal",self
    """
    En vista a esto, los métodos de instancia:

    Pueden acceder y modificar los atributos del objeto.
    Pueden acceder a otros métodos.
    Dado que desde el objeto self se puede acceder 
    a la clase con ` self.class`, también pueden modificar el estado de la clase
    """ 
    @classmethod
    def metodoclase(cls):
        return "Metodo de Clase",cls
        """
        A diferencia de los métodos de instancia, los métodos de 
        clase reciben como argumento cls, que hace referencia a la clase.
        Por lo tanto, pueden acceder a la clase pero no a la instancia.
        No pueden acceder a los atributos de la instancia.
        Pero si pueden modificar los atributos de la clase.
        """
    
    @staticmethod
    def metodoestatico():
        return "Metodo Estatico"
        """
        Por último, los métodos estáticos se pueden definir
        con el decorador @staticmethod y no aceptan como parámetro ni la instancia ni la clase. Es por ello por lo que no pueden modificar el estado ni de la clase ni de la instancia.
        Pero por supuesto pueden aceptar parámetros de entrada.
        """