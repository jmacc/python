#Clain Class

class Punto:
    def __init__(self, x , y):
        self.X = x
        self.Y = y
    
    def MostrarPunto(self):
        print("El punto es (",self.X,",",self.Y,")")
        
p1 = Punto(2,3)
p1.MostrarPunto()