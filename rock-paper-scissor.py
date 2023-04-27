class Participant:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ""
        print("Bienvenido: {participante}".format(participante = self.name))

    def choose(self):
        self.choice = input("{name}, select rock, paper o scisssor: ".format(name = self.name))
        print("{name}, selects {choice}".format(name = self.name,choice = self.choice))

# seleccion de opcion en pantalla
# Inicia Juego
class Decoration:
    def __init__(self):
            self.deco = print(('**********'))
            self.welcome = print("Bienvenido:\n")
            
class gameRound:
    def __init__(self,p1,p2):

         p1.choose()
         p2.choose()
         
         
class Game:
    def __init__(self):
        self.endGame = False 
        self.participant= Participant(
        input("Ingresar el nombre del Primer Participante: ")) # Agrugar a los participantes
        self.secondParticipant = Participant(
        input("Ingrese el nombre del Segundo Participante: ")) # Agregar a los participantes
        
    def start(self):
       # while not self.endGame:
            game_round = gameRound(self.participant, self.secondParticipant)
            

decoracion = Decoration()
decoracion.deco
decoracion.welcome
decoracion.deco
game = Game()
game.start
