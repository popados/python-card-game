class turnCounter ():


    def __init__(self, turns, mana, nextPlayer, currentPlayer) :
        self.turns = turns
        self.mana = mana
       # self.health = health
        self.nextPlayer = nextPlayer
        self.currentPlayer = currentPlayer

    def printTurns(self):
        print("turns: " , self.turns)
        print("mana: " , self.mana)
        print("current health: " , self.currentPlayer.health)
        print("next player health: ", self.nextPlayer.health)
        print("current player: " , self.currentPlayer.name)
        print("next player: ", self.nextPlayer.name)

    def addTurnCount(self, currentPlayer):
        #print(self.turns)
        self.turns += 1
        currentPlayer.count += 1

    def changePlayer(self, currentPlayer, nextPlayer):
        self.currentPlayer = self.currentPlayer
        print(self.currentPlayer.health)
        self.nextPlayer = self.nextPlayer
        print(self.nextPlayer.health)
        self.nextPlayer = self.currentPlayer
    