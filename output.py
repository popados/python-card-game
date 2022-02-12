from asyncio.windows_events import NULL
from unicodedata import name
import arithmetic_operations
from string_functions import first_name
import string_functions
from card import card


your_name = ''

x = input("enter a number \n")

y = input ("enter a second number \n")

z = 0

# Function calls to ask and print your name
#

string_functions.ask_name(your_name)

your_name = string_functions.first_name(your_name)

print(your_name)

# funnction calls to ask for numbers and print the numerical operation


arithmetic_operations.add_nums(x, y)

arithmetic_operations.subtract_nums(x,y)

arithmetic_operations.divide_nums(x,y)

z = arithmetic_operations.multiply_nums(x,y)

print(z)

goblin = card("monster", "2","3")
fireball = card("spell", "1", NULL)

print("goblin card:")
goblin.showCard()

print("fireball card:")
fireball.showCard()

# thirdName = input("what is your name ")
# print(thirdName)

#firstname = input('first name?: ')

#string_functions.first_name(firstname)

# sentence = input("enter a panagram :\n")


# if (string_functions.panagram_check(sentence) == True) :
#     print("this contains all letters in the alphabet")

# else :
#     print ("this does not have all the letters.")

# hi = 'hello'

# print(hi)

# print("hi")