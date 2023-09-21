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
        print("health: " , self.currentPlayer.health)
        print("player: " , self.nextPlayer.name)

