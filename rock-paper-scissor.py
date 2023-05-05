class Participant:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ""
        print("Bienvenido: {participante}".format(participante=self.name))

    def choose(self):
        self.choice = input(
            "{name}, select rock, paper or scissor: ".format(name=self.name))
        print("{name} selects {choice}".format(
            name=self.name, choice=self.choice))

    def toNumericalChoice(self):
        switcher = {
            "rock": 0,
            "paper": 1,
            "scissor": 2
        }
        return switcher[self.choice]


class GameRound:
    def __init__(self, p1, p2):  # recibe los nombres
        self.rules = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]
        p1.choose()
        p2.choose()
        #Valores en memoria
        print(p1, " , ", p2)
        result = self.compareChoices(p1,p2)
        # print("Numerical Choise {numerical}".numerica2)
        # print("Rounded Result in a {result}".format(result = self.getResultAsString(result)))
        # print("Rounded Result in a {result}".format(result = self.getResultAsString()))
        

    def compareChoices(self, p1, p2):
        return self.rules[p1.toNumericalChoise()][p2.toNumericalChoice()]

    def awardPoints(self):
        print("implement")

    def getResultAsString(self, result):
        res = {0: "draw", 1: "win", -1: "loss"}
        return res[result]


class Decoration:
    def __init__(self):
        self.deco = print(10 * "*")
        self.welcome = print("Bienvenido:\n")


class Game:
    def __init__(self):
        self.endGame = False
        self.participant = Participant(
            input("Ingresar el nombre del Primer Participante: "))  # Agrugar a los participantes
        self.secondParticipant = Participant(
            input("Ingrese el nombre del Segundo Participante: "))  # Agregar a los participantes

    def start(self):
        game_round = GameRound(self.participant, self.secondParticipant)

    def checkEndCondition(self):
        print("implement")

    def determineWinner(self):
        print("implement")


dec = Decoration()
dec.deco
dec.welcome
game = Game()
game.start()
