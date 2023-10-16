
# from card_object import card
# from commander_object import commander

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

    def dealDamage(player, damage) :
        # health = player.health
        health = player.health
        damage = damage.attack
        player.health -= damage
        print("you did:", damage)
        print(player.health)
        return health


#Doesnt work    
#    def cardName(self) :
#        print("card name is", )
