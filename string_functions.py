
# first_name = 'this'
# print(first_name)
# def first_name() :
#     first_name = input("what is your first name: ")
#     return first_name
# # first_name()

# print(first_name())
# #print(name)



def first_name(name) :
    print("your first name is :",name)

def panagram_check(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for char in alphabet :
        if char not in sentence.lower() :
            return False
        return True

