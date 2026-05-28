#Allison Luo
#Dog Breed
#The purpose of my program is to help users choose a dog breed that meets their needs.

#Initialize
import pandas as pd
import random
import webbrowser

data = pd.read_csv('dog.csv')

id = data['id'].tolist()
name = data['Name'].tolist()
breed = data['Breed Group'].tolist()
weight = data['Minimum Weight'].tolist()
temp = data['Temperament'].tolist()
image = data['Image'].tolist()
bredfor = data['BredFor'].tolist()

dogs = []
temper = []
traits = []

#Functions
def menu():
    print("Hello! This is our game to help you find which dog is best suited for you!")
    while True:
        choose = input("What do you want to see? Do you want to find a dog based on your size preference (size), the temperament of the dog (temperament), the traits of the dog (trait), or exit (exit)?: ")
        if choose == "size":
            size = input("What size of a dog do you want? (tiny, small, medium, or large): ")
            getDogSize(size)
        elif choose == "temperament":
            breed_name = input("Please type the name of the dog you want to see: ")
            lookup(breed_name)
        elif choose == "trait":
            purpose = input("What dog trait do you want to look up?: ")
            trait(purpose)
        elif choose == "exit":
            break

def getDogSize(size):
    if size == "tiny":
        for i in range(len(name)):
            if weight[i] <= 10:
                dogs.append(name[i])
        print(f"We recommend the {dogs[random.randint(0, 11)]} dog!")
        print(f"If you do not like this dog, we have these other tiny dogs you can choose from. Here is the list of dogs: {dogs}")
        dogs.clear()
    elif size == "small":
        for i in range(len(name)):
            if weight[i] >= 11 and weight[i] <= 25:
                dogs.append(name[i])
        print(f"We recommend the {dogs[random.randint(0, 11)]} dog!")
        print(f"If you do not like this dog, we have these other tiny dogs you can choose from. Here is the list of dogs: {dogs}")
        dogs.clear()
    elif size == "medium":
        for i in range(len(name)):
            if weight[i] >= 26 and weight[i] <= 60:
                dogs.append(name[i])
        print(f"We recommend the {dogs[random.randint(0, 11)]} dog!")
        print(f"If you do not like this dog, we have these other tiny dogs you can choose from. Here is the list of dogs: {dogs}")
        dogs.clear()
    elif size == "large":
        for i in range(len(name)):
            if weight[i] > 60:
                dogs.append(name[i])
        print(f"We recommend the {dogs[random.randint(0, 11)]} dog!")
        print(f"If you do not like this dog, we have these other tiny dogs you can choose from. Here is the list of dogs: {dogs}")
        dogs.clear()
    else:
        print("We do not have any dogs that suit what you want.")

def lookup(breed_name):
    if breed_name in name:
        for i in range(len(name)):
            if breed_name in name[i]:
                temper.append(temp[i])
                picture = image[i]
        print(f"{breed_name} is {temper}")
        webbrowser.open(picture)
        temper.clear()
    else:
        print("Sorry, we do not have the do you want.")

def trait(purpose):
    for i in range(len(bredfor)):
        if purpose in bredfor[i]:
            traits.append(name[i])
    if traits == []:
        print("There is none")
    else:
        print(f"If your purpose is {purpose}, we recommend {traits}!")
    traits.clear()

#Main
menu()

#Sources
#Dog Dataset
#Website Name: Code.org
#URL: https://code.org/en-US
#Dataset Source: https://thedogapi.com/en

