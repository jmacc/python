#Modify Class

class Punto:
    def __init__(tec,x,y):
        tec.X = x
        tec.Y = y
    def mostrarPunto(tec):
        print("Impresion: ",tec.X, "," ,tec.Y)
        
p1 = Punto(4,6)
p1.mostrarPunto()

p1.X = 12
p1.Y = 23

p1.mostrarPunto()