from card_object import card
from commander_object import commander

goblin = card("goblin", "monster", 3, 1)

fireball = card("fireball", "spell", int(2), 0)

playerOne = commander("player one", int(5), int(20))

#goblin.showCard()
# global hitpoints
# global health
# global damage

commanderAlive = False

damage = 1

global hitpoints

hitpoints = playerOne.health
print("your hp is:", hitpoints)
totalhealth = int(20)

# Put into new object called Avatar or Commander
# 

def varSubtract(var):
    return int(var) - int(damage)

def dealDamage():
    global health
    health = health - 1
    print("damage to global health var :", health)

# def loseHitpoints( health , damage):
#     #global hitpoints

#     health = health - damage
#     print("same")
#     print("damage to global hitpoints var:", damage)


def loseHitpoints(damage) :
    global hitpoints
    hitpoints = hitpoints - damage
    print("you did:", damage)

# THIS IS MY MAIN LOGIC I GUESS(?)

if (totalhealth >= hitpoints):
    
    print("health is greater than or equal to hitpoints")
    #fireball.loseHitpoints(damage)
    fireball.loseHitpoints(hitpoints, fireball.attack )
    print("your hp is:", hitpoints)


else :

    print("i got here")

# if (int(health) >= int(hitpoints)):
#     commanderAlive = True

#     while commanderAlive == True :
#         #loseHitpoints(playerOne.health)
#         fireball.loseHitpoints(hitpoints)
#         if int(hitpoints <= 0 ) : 
#             commanderAlive = False

print("end of program")






# commanderAlive = True
# print("health", health)

# if commanderAlive == True:
#     dealDamage()
#     print("health", health)

    # if (health <= 0):
    #     commanderAlive = False
    #     print("dead")
# elif (commanderAlive == False):
#     print("you are dead")

# print("if statement done")

# print("this is health: ", health)
# print("this is hitpoints :", hitpoints)

# dealDamage()
# loseHitpoint()

# print(health)
# print(hitpoints)

# if (opponent > 0):
#     print(health)
#     dealDamage(opponent)
# elif (health < 0):
#     print("opponent defeated")






# var = int(20)

# varSubtract(var)

# print (var)