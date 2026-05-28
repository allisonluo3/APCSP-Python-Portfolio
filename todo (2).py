#Allison
#To-Do List
#Create the To-do List App that allows the user to keep track of items that must get done during the day.
#Initialize
#Functions
groceries = ["Steak", "Chicken", "Apples", "Bananas", "Eggs", "Pasta"]
done = []


def list():
    print(f"Here is grocery list: {groceries}")
    while True:
        option = input("What would you like to do today! (Add, Done, Remove, Clear, or Exit): ")
        if option == "Add":
            add = input("What would you like to add?: ").strip()
            if add == "":
                print("Sorry, I don't understand.")
            else:
                groceries.append(add)
                print(f"This is your current grocery list: {groceries}")
                print(f"This is your done grocery list: {done}")
            continue
        elif option == "Done":
            complete = input("What item would you like to mark as done?: ")
            if complete in groceries:
                groceries.remove(complete)
                done.append(complete)
                print(f"This is your current grocery list: {groceries}")
                print(f"This is your done grocery list: {done}")
            else:
                print("Sorry. This item is not in your list.")
            continue
        elif option == "Remove":
            removing = input(f"Here is your list right now, {groceries}. What item would you like to remove?: ")
            try:
                groceries.remove(removing)
                print(f"Here is your current grocery list: {groceries}")
                print(f"Here is your done grocery list: {done}")
            except:
                print("This item is not on your list")
                continue
        elif option == "Clear":
            groceries.clear()
            print(f"This is your current grocery list: {groceries}")
        elif option == "Exit":
            print(f"This is your current grocery list: {groceries}")
            print(f"This is your done grocery list: {done}")
            break
        else:
            print("Sorry, I don't understand.")
            continue
#Main
list()
