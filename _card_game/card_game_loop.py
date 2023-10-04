from card_object import card
from commander_object import commander
from cg_turn_count import turnCounter

goblin = card("goblin", "monster", int(3), int(1))

fireball = card("fireball", "spell", int(2), int(1))

playerOne = commander("player one", int(5), int(20), 0)

playerTwo = commander("player two", int(5), int(20), 0)

gameCount = turnCounter(0, 1, 20, playerTwo, playerOne)



commanderAlive = True


def varSubtract(var):
    return int(var) - int(1)

def dealDamage():
    #global totalhealth
    totalhealth = playerOne.health
    totalhealth - 1
    #loseHitpoints(damage)
    print("damage to global health var :", totalhealth)


def playerOneTurn(commander: playerOne):
    print()
    counter = playerOne.count


    # # counter = count
    print("player one turn " + str(counter))
    playerOne.loseHitpoints(playerOne, fireball)
    print()
    print("Press Enter to End Turn")
    input()


def playerTwoTurn(commander: playerTwo):
    print()
    counter = playerTwo.count


    # # counter = count
    print("player two turn " + str(counter))
    playerOne.loseHitpoints(playerTwo, fireball)
    print()
    print("Press Enter to End Turn")
    input()

def turnCounter():

    if commanderAlive == True:
            
        while commanderAlive == True:
            #dealDamage()
            #function does not return health correctly
            #works now
            #   
            gameCount.printTurns()
            print()
            # gameCount.printTurns()

            print("pick 1 for player 1. press 2 for player 2")
            selection = input()
            if selection == "1":

                playerOne.count += 1
                playerOneTurn(playerOne)
            # playerOne.count + 1
            if selection == "2":
                playerTwo.count += 1
                playerTwoTurn(playerTwo)
            if (playerOne.health <= 0):
                commanderAlive == False
                print("player 2 wins")
                break
            if (playerTwo.health <= 0):
                commanderAlive == False
                print("player 1 wins")
                break
            else:
                continue
            # playerOne.health -= 1
            # print(playerOne.health)


turnCounter()
print("end of program")

#goblin.showCard()
# global hitpoints
# global health
# global damage


# damage = 1

#global hitpoints

# hitpoints = playerOne.health
# print("your hp is:", hitpoints)
#totalhealth = int(20)

# Put into new object called Avatar or Commander
# 



# def loseHitpoints( health , damage):
#     #global hitpoints

#     health = health - damage
#     print("same")
#     print("damage to global hitpoints var:", damage)
# global playerOne
# global hitpoints


#the overload is the key here 
# def loseHitpoints(player: commander, damage:card) :
#     # health = player.health
#     health = player.health
#     damage = damage.attack
#     player.health -= damage
#     print("you did:", damage)
#     print(player.health)
#     return health




# while True:



# THIS IS MY MAIN LOGIC I GUE~SS(?)

# if (totalhealth >= hitpoints):
    
#     print("health is greater than or equal to hitpoints")
#     #fireball.loseHitpoints(damage)
#     fireball.loseHitpoints(hitpoints, fireball.attack )
#     print("your hp is:", hitpoints)


# else :

#     print("i got here")

# START GAME




#game loop


    #player 1 turn
    #PLAYER 2 turn
    
    


# if (int(health) >= int(hitpoints)):
#     commanderAlive = True

#     while commanderAlive == True :
#         #loseHitpoints(playerOne.health)
#         fireball.loseHitpoints(hitpoints)
#         if int(hitpoints <= 0 ) : 
#             commanderAlive = False






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