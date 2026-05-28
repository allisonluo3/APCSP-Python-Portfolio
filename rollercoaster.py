#Purpose: This program helps users decide which rollercoaster is best for them based on their preferences
#Rollercoaster Finder

#Initialize
import pandas as pd
import random
import webbrowser
import time

data = pd.read_csv('rollercoaster.csv')

location = data['Amusement Park'].tolist()
city = data['City'].tolist()
country = data['Country'].tolist()
height = data['Height'].tolist()
speed = data['Speed'].tolist()
length = data['Length'].tolist()
rollercoaster = data['Rollercoaster Name'].tolist()

#Images of coasters
image = ["https://rcdb.com/aadatre", "https://tinyurl.com/2m74pmut",
         "https://tinyurl.com/57y6j2d4","https://tinyurl.com/3emb6zcu"]

#Categories of each rollercoaster
kiddie = []
family = []
mega = []
hyper = []

#Categories for the speed types according to the category of rollercoaster
slow = []
moderate = []
fast = []
extreme = []

#Categories for the ride's duration according to the category of rollercoaster
short = []
average = []
long = []
extremely_long = []

#Functions
print("-------------------------------------------------------------------------------------------------------------")
print("Hello! Welcome to CoasterFinder! This is my game to help you find which rollercoaster is best suited for you!")
print("-------------------------------------------------------------------------------------------------------------")
def menu():
    organize()
    while True:
        ask = input("Do you want a recommendation for a rollercoaster ride (Yes, No): ").lower()
        if ask == "yes":
            options = input("To find the perfect rollercoaster for you, please choose an option here to filter by: Your Height and Age (H&A), Speed of Ride (Speed), Height of Ride (Height), Duration of Ride (Time), Generate a Random Ride (Generate), View Popular Images of Rollercoasters (View), or Leave (Exit): ").lower()
            if options == "h&a":
                age = int(input("How old are you?: "))
                if age <= 3:
                    print("Sorry, you are too young to ride a rollercoaster.")
                    break
                elif age > 3:
                    height_age(age)
            elif options == "speed":
                rate = input("What speed do you want your rollercoaster to be at? (slow, moderate, fast, extreme): ")
                speeds(rate)
            elif options == "height":
                type = input("How high up are you willing to go? Kiddie: up to 26 feet, Family: up to 60 feet, Mega: up to 100 feet, Hyper: up to 130 feet: Please enter your choice (Kiddie, Family, Mega, Hyper): ").lower()
                ride_height(type)
            elif options == "time":
                time = input("How long do you want your ride to last? (Short, Average, Long, Extremely Long): ").lower()
                duration(time)
            elif options == "generate":
                generate()
            elif options == "view":
                popular_choices()
            elif options == "exit":
                print("We're sad to see you go. We hope to see you again!")
                break
        elif ask == "no":
            print("Goodbye! See you next time!")
            break
        else:
            print("That's not an option! Please try again.")
            continue

#Assigns rollercoasters into an array depending on what kind of rollercoaster it is (ex: kidde, family, mega, hyper)
def organize():
    for i in range(len(rollercoaster)):
        if height[i] <= 26:
            kiddie.append(rollercoaster[i])
        elif height[i] > 26 and height[i] <= 60:
            family.append(rollercoaster[i])
        elif height[i] > 60 and height[i] <= 100:
            mega.append(rollercoaster[i])
        elif height[i] > 100 and height[i] <= 130:
            hyper.append(rollercoaster[i])

#This function plays if the user wants to find a rollercoaster based on their height and age
def height_age(age):
    if age > 3:
        yourheight = float(input("What is your height in feet? (3-4, 4-4.5, 4.5-7): "))
        if 3 <= yourheight <= 4:
            print("Great! You are tall enough to ride the kiddie coaster!")
            print(f"We recommend the {random.choice(kiddie)}, a kiddie rollercoaster less than 26 feet tall.")
        elif 4 < yourheight <= 4.5:
            print("Great! You are tall enough to ride the family coaster!")
            print(f"We recommend the {random.choice(family)}, a family rollercoaster between 26 and 60 feet tall.")
        elif yourheight > 4.5:
            print("Great! You are able to ride the mega, and hyper coasters!")
            choose = input("Do you want to ride the mega rollercoaster (mega) or hyper rollercoaster (hyper)?: ").lower()
            if choose == "mega":
                print(f"We recommend the {random.choice(mega)}, a mega rollercoaster between 60 and 100 feet tall.")
            elif choose == "hyper":
                print(f"We recommend the {random.choice(hyper)}, a hyper rollercoaster between 100 and 130 feet tall.")
        else:
            print("Sorry, try again.")

#This function plays if the user wants to find a rollercoaster based on how fast they want their rollercoaster to be
def speeds(rate):
    for i in range(len(rollercoaster)):
        if speed[i] <= 30:
            slow.append(rollercoaster[i])
        elif speed[i] > 30 and speed[i] <=65:
            moderate.append(rollercoaster[i])
        elif speed[i] > 65 and speed[i] <= 100:
            fast.append(rollercoaster[i])
        elif speed[i] > 100:
            extreme.append(rollercoaster[i])
    if rate == "slow":
        rand_slow = random.choice(slow)
        print(f"We recommend the {random.choice(slow)} rollercoaster. This rollercoaster goes from 9-30 mph.")
    elif rate == "moderate":
        rand_moderate = random.choice(moderate)
        print(f"We recommend the {random.choice(moderate)} rollercoaster. This rollercoaster goes from 30-65 mph.")
    elif rate == "fast":
        rand_fast = random.choice(fast)
        print(f"We recommend the {random.choice(fast)} rollercoaster. This rollercoaster goes from 65-100 mph.")
    elif rate == "extreme":
        rand_extreme = random.choice(extreme)
        print(f"We recommend the {random.choice(extreme)} rollercoaster. This rollercoaster goes from 100-195 mph.")
    else:
        print("Sorry, please try again.")

#This function plays if the user wants to find a rollercoaster based on the maximum height they are willing to be on the rollercoaster
def ride_height(type):
    if type == "kiddie":
        print(f"We recommend the {random.choice(kiddie)}, a kiddie rollercoaster less than 26 feet tall.")
    elif type == "family":
        print(f"We recommend the {random.choice(family)}, a family rollercoaster between 26 and 60 feet tall.")
    elif type == "mega":
        print(f"We recommend the {random.choice(mega)}, a mega rollercoaster between 60 and 100 feet tall.")
    elif type == "hyper":
        print(f"We recommend the {random.choice(hyper)}, a hyper rollercoaster between 100 and 130 feet tall.")
    else:
        print("Sorry, please try again.")

#This function plays if the user wants to find a rollercoaster based on the maximum duration they are willing to be on the rollercoaster
def duration(time):
    for i in range(len(rollercoaster)):
        if length[i] >= 60 and length[i] <= 300:
            short.append(rollercoaster[i])
        elif length[i] > 300 and length [i] <= 600:
            average.append(rollercoaster[i])
        elif length[i] > 600 and length[i] <=1200:
            long.append(rollercoaster[i])
        elif length[i] > 1200:
            extremely_long.append(rollercoaster[i])
        else:
            print("Sorry, please try again.")
    if time == "short":
        print(f"We recommend the {random.choice(short)}. This ride will last approximately 45 seconds. ENJOY!")
    elif time == "average":
        print(f"We recommend the {random.choice(average)}, This ride will last approximately 1.5-2 minutes. ENJOY!")
    elif time == "long":
        print(f"We recommend the {random.choice(long)}, This ride will last approximately 3-4 minutes. ENJOY!")
    elif time == "extremely long":
        print(f"We recommend the {random.choice(extremely_long)}, This ride will last approximately 5-6 minutes. ENJOY!")

#This function plays if the user wants to find a rollercoaster randomly from the database. This does not consider any outside factors from the user.
def generate():
    while True:
        print("We are currently choosing a rollercoaster for you. Please wait a moment.")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        coaster = random.choice(rollercoaster)
        print(f"We recommend the {coaster}.")
        satisfied = input("Are you satisfied with your choice? (Yes, No): ").lower()
        if satisfied == "yes":
            break
        elif satisfied == "no":
            print("No problem! Let's choose another one.")
            continue

#This function plays if the user wants to view some images of our popular rollercoasters
def popular_choices():
    popular = input("Would you like to view some pictures of some of our most popular rollercoasters? (Yes, No): ").lower()
    if popular == "yes":
        picture = input("What kind of popular rollercoaster are you interested in viewing? (Kiddie, Family, Mega, Hyper): ").lower()
        if picture == "kiddie":
            webbrowser.open(image[0])
            print("Here is some information about Conccinelle!")
            print(data.loc[36])
            print("This is a kid-friendly rollercoaster that’s perfect for those who are afraid of heights, offering a fun and enjoyable experience for younger children!")
        elif picture == "family":
            webbrowser.open(image[1])
            print("Here is some information about Giant Dipper!")
            print(data.loc[118])
            print("This family-friendly rollercoaster sits near the beach and reaches moderate heights, making it a great option for those who want some excitement without going too high!")
        elif picture == "mega":
            webbrowser.open(image[2])
            print("Here is some information about Goliath!")
            print(data.loc[247])
            print("This mega rollercoaster reaches towering heights while offering a slightly less intense experience than hyper coasters, making it a great step up for more experienced riders!")
        elif picture == "hyper":
            webbrowser.open(image[3])
            print("Here is some information about Top Thrill Dragster!")
            print(data.loc[252])
            print("This hyper rollercoaster is perfect for thrill-seekers, delivering extreme heights and nonstop motion for those ready for an intense ride!")
    elif popular == "no":
        print("Goodbye! See you next time!")
        return

#Main
menu()

#Sources
#Rollercoaster Dataset
#Website Name: Code.org
#URL: https://tuvalabs.com/datasets/?type=datasets&order_by=-pub_date&show=all
#Dataset Source: https://tuvalabs.com/datasets/?type=datasets&order_by=-pub_date&show=all

#Coccinelle Kiddie Rollercoaster
#Website Name: RCDB
#Photographers: https://rcdb.com/about.htm
#URL: https://rcdb.com/946.htm

#Giant Dipper Family Coaster
#Website Name: Secret San Francisco
#Author: Jamie Ferrell
#URL: https://secretsanfrancisco.com/santa-cruz-boardwalk-giant-dipper/
#Date: November 15, 2021

#Goliath Mega Rollercoaster
#Title: It’s hard to top Goliath at Six Flags Great America
#Website Name: AboutThemeParks
#Author: Arthur Levine
#URL: https://www.aboutthemeparks.fun/p/its-hard-to-top-goliath-at-six-flags
#Date: July 20, 2023

#Rollercoaster Top Thrill Dragster Hyper Coaster
#Title: Cedar Point fans determined to uncover secrets behind Top Thrill Dragster's new design
#Website Name: Detroit Free Press
#Author: Frank Witsil
#URL: https://www.freep.com/story/news/local/michigan/2023/07/30/top-thrill-dragster-cedar-point-ohio-clues-amusement-park/70419761007/?gnt-cfr=1&gca-cat=p&gca-uir=false&gca-epti=z114301u115701e1122xxv114301&gca-ft=245&gca-ds=sophi
#Date: July 28, 2023
