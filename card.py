


class card () :

    def __init__ (self, type, attack, health) :
        self.type = type
        self.attack = attack
        self.health = health

    def showCard(self) :
        print("Type is", self.type)
        print("Attack is", self.attack)
        print("Health is", self.health)
            
