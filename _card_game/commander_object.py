
##  Imports
# 


## Creation of commander or avatar
#

class commander ():

    def __init__ (self, name, attack, health, count) :
        self.name = name
        self.attack = attack
        self.health = health
        self.count = count

    # def loseHitpoints(hitpoints):
    #     #global hitpoints
    #     hitpoints = hitpoints - 1
    #     print("same")
    #     print("damage to global hitpoints var:", hitpoints)
    def dealDamage(self, player, damage) :
        # health = player.health
        health = player.health
        damage = damage.attack
        player.health -= damage
        print("you did:", damage)
        print("health remaining:", player.health)
        return health





