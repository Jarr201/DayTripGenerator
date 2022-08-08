import random


destination = ["The Bahamas", "Tokyo", "New York", "Florida", "Italy", "Los Angeles", "Athens"]
restuarant = ["fast food place", "buffet", "diner", "bar", "food truck", "street food market"]
transportation = ["train", "airplane", "car", "cruise ship", "skateboard", "bicycle"]
entertainment  = ["nature walk", "shopping spree", "city tour", "beach visit", "museum visit", "boat ride", "theme park visit"]

def begin(intro = "Hello and Welcome to your trip planner! Lets get you started!"):
    print(intro)

begin()

def Trip_component():
    trip_dest = random.choice(destination)
    trip_rest = random.choice(restuarant)
    trip_trans = random.choice(transportation)
    trip_enter = random.choice(entertainment)
    full_trip = f"You'll be visiting {trip_dest} via {trip_trans}. During your trip, you should eat at a {trip_rest} and go on a {trip_enter} while you're out!"
    print(full_trip)
    return

Trip_component()

def reroll():
    request = input("What would you like to change? Reply with Destination, Restuarant, Transportation, or Entertainment. ")
    if request == "Destination":
        trip_dest = random.choice(destination)
        answer = input(f"Would you prefer going to {trip_dest}? Y/N ")
        if answer == "Y":
            confirmation()
        elif answer == "N":
            reroll()
        else:
            print("Sorry. Please answer again in the correct format. ")
            confirmation()
    elif request == "Restuarant":
        trip_rest = random.choice(restuarant)
        answer = input(f"Would you prefer eating at a {trip_rest}? Y/N ")
        if answer == "Y":
            confirmation()
        elif answer == "N":
            reroll()
        else:
            print("Sorry. Please answer again in the correct format. ")
            confirmation()
    elif request == "Transportation":
        trip_trans = random.choice(transportation)
        answer = input(f"Would you prefer traveling via {trip_trans}? Y/N ")
        if answer == "Y":
            confirmation()
        elif answer == "N":
            reroll()
        else:
            print("Sorry. Please answer again in the correct format. ")
            confirmation()
    elif request == "Entertainment":
        trip_enter = random.choice(entertainment)
        answer = input(f"Would you prefer going on a {trip_enter}? Y/N ")
        if answer == "Y":
            confirmation()
        elif answer == "N":
            reroll()
        else:
            print("Sorry. Please answer again in the correct format. ")
            confirmation()
    else:
        print("Sorry. Please answer again in the correct format. ")
        confirmation()
    return

def confirmation():
    inquiry = input("Do you like your trip? Y/N ")
    if inquiry == "Y":
        print("We're glad you're satisfied! Have a great trip!")
        print("Program Complete!")
    elif inquiry == "N":
        print("No problem! Let's make this plan work for you.")
        reroll()
    else:
        print("Sorry. Please answer again in the correct format. ")
        confirmation()
    return inquiry
 
confirmation()