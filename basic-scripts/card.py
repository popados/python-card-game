


class card () :

    def __init__ (self, name, type, attack, health) :
        self.name = name
        self.type = type
        self.attack = attack
        self.health = health

    def showCard(self) :
        print("Name is", self.name)
        print("Type is", self.type)
        print("Attack is", self.attack)
        print("Health is", self.health)

#Doesnt work because you should not try to get the variable name of an object
#    def cardName(self) :
#        print("card name is", )
