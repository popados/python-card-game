
##  Imports
# 


## Creation of commander or avatar
#

class commander ():

    def __init__ (self, name, attack, health) :
        self.name = name
        self.attack = attack
        self.health = health

    def loseHitpoints(hitpoints):
        #global hitpoints
        hitpoints = hitpoints - 1
        print("same")
        print("damage to global hitpoints var:", hitpoints)




