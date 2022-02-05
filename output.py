import arithmetic_operations
import string_functions


x = input("enter a number \n")

y = input ("enter a second number \n")

z = 0

arithmetic_operations.add_nums(x, y)

arithmetic_operations.subtract_nums(x,y)

arithmetic_operations.divide_nums(x,y)

arithmetic_operations.multiply_nums(x,y)

name = input('first name?: ')

string_functions.first_name(name)

sentence = input("enter a panagram :\n")


if (string_functions.panagram_check(sentence) == True) :
    print("this is contains all words in the alphabet")

else :
    print ("this does not have all the words.")

# hi = 'hello'

# print(hi)

# print("hi")