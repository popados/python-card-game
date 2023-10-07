class turnCounter ():


    def __init__(self, turns, mana, health, nextPlayer, currentPlayer) :
        self.turns = turns
        self.mana = mana
        self.health = health
        self.nextPlayer = nextPlayer
        self.currentPlayer = currentPlayer

    def printTurns(self):
        print("turns: " , self.turns)
        print("mana: " , self.mana)
        print("current health: " , self.currentPlayer.health)
        print("next player health: ", self.nextPlayer.health)
        print("current player: " , self.nextPlayer.name)
        print("next player: ", self.currentPlayer.name)


    def addTurnCount(self):
        #print(self.turns)
        self.turns += 1
