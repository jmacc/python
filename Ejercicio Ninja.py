#Ejercicio Ninja

class NinjaPrincipal:
    #valores por defecto
    poder = 100
    resistencia = 50
    vidas = 1
    
    def game_over(self):
        print("Game over")
        
#creamos el objeto a partir de la clase
ninja1 = NinjaPrincipal()
ninja2 = NinjaPrincipal()

#asignammos valores diferentes
ninja1.poder = 200
ninja2.poder = 300

#mostramos los valores
print(ninja2.poder)
print(ninja2.resistencia)
print(ninja2.vidas)

class Tortugas:
    def __init__(self, hp, resistencia, xp, vidas):
        self.hp = hp
        self.resistencias = resistencia
        self.xp = xp
        self.vidas = vidas
        
#creamos el objeto
tortuga1 = Tortugas()
tortuga1.xp = 12
tortuga1.resistencias = 12
tortuga1.hp = 12
tortuga1.vidas = 1
print(tortuga1.hp, tortuga1.resistencias, tortuga1.xp, tortuga1.vidas)