from card_object import card

goblin = card("goblin", "monster", 3, 1)

fireball = card("fireball", "spell", 2, 0)

#goblin.showCard()
global hitpoints
global health

hitpoints = 0
health = int(20)

def varSubtract(var):
    return int(var) - int(1)

def dealDamage():
    global health
    health = health - 1
    print("damage to global health var :", health)

def loseHitpoint():
    global hitpoints
    hitpoints - 1
    print("damage to global hitpoints var :", hitpoints)


print("this is health: ", health)
print("this is hitpoints :", hitpoints)

dealDamage()
loseHitpoint()

print(health)
print(hitpoints)

# if (opponent > 0):
#     print(health)
#     dealDamage(opponent)
# elif (health < 0):
#     print("opponent defeated")






# var = int(20)

# varSubtract(var)

# print (var)