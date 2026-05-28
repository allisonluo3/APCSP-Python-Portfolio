#Allison
#Hogwarts
#Create a program that prompts the user for their name and simulates being assigned one of the 4 hogwarts houses

#Initialize
import time
import random

#Function
def main():
    print("Welcome to Hogwarts")
    name = input("What is your name: ")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("....")
    print( house(name) )

def house(name):
    if name == "Harry" or name == "Ron" or name == "Hermione":
        return "Gryffindor"
    elif name == "Newt" or name == "Nymphadora" or name == "Pomona":
        return "Hufflepuff"
    elif name == "Luna" or name == "Cho" or name == "Filius":
        return "Ravenclaw"
    elif name == "Voldemort" or name == "Draco" or name == "Severus":
        return "Slytherin"
    else:
        school = random.randint(1,4)
        if school == 1:
            return "Gryffindor"
        elif school == 2:
            return "Hufflepuff"
        elif school == 3:
            return "Ravenclaw"
        elif school == 4:
            return "Slytherin"

#Main
main()
