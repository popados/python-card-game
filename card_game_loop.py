from distutils import command
from card_object import card

goblin = card("goblin", "monster", 3, 1)

fireball = card("fireball", "spell", 2, 0)

#goblin.showCard()
global hitpoints
global health
global damage

commanderAlive = False

damage = 1

hitpoints = int(20)
print("your hp is:", hitpoints)
health = int(20)

def varSubtract(var):
    return int(var) - int(damage)

def dealDamage():
    global health
    health = health - 1
    print("damage to global health var :", health)

def loseHitpoints():
    global hitpoints
    hitpoints = hitpoints - 1
    print("same")
    print("damage to global hitpoints var:", hitpoints)


# THIS IS MY MAIN LOGIC I GUESS(?)

if (int(health) >= int(hitpoints)):
    commanderAlive = True

    while commanderAlive == True :
        loseHitpoints()

        if int(hitpoints) <= 0 : 
            commanderAlive = False

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