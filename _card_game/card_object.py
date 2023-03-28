


class card () :

    def __init__ (self, name, type, attack, health) :
        self.name = name
        self.type = type
        self.attack = attack
        self.health = health
        self.isSpell = False
        self.isCreature = False
        self.isCastable = True

    def showCard(self) :
        print("Name is", self.name)
        print("Type is", self.type)
        print("Attack is", self.attack)
        print("Health is", self.health)

    def loseHitpoints(self, hitpoints, damage):
        damage = damage
        hitpoints = hitpoints - damage
        print("from card object")
        print("damage to global hitpoints var:", damage)
        print(hitpoints)
        return (hitpoints)


#Doesnt work    
#    def cardName(self) :
#        print("card name is", )
