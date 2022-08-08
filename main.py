import random

destination = ["the Bahamas", "Tokyo", "New York", "Florida"]
restuarant = ["fast food place", "buffet", "diner", "bar"]
transportation = ["train", "airplane", "car", "cruise ship"]
entertainment  = ["nature walk", "shopping spree", "city tour", "beach visit"]

intro = "Hello and Welcome to your trip planner! Lets get you started!"
print(intro)

trip_dest = random.choice(destination)
trip_rest = random.choice(restuarant)
trip_trans = random.choice(transportation)
trip_enter = random.choice(entertainment)


full_trip = f"You'll be visiting {trip_dest} via {trip_trans}. During your trip, you should eat at a {trip_rest} and go on a {trip_enter} while you're out!"
print(full_trip)

inquiry = input("Do you like your trip? Y/N ")

if inquiry == "Y":
    print("We're glad you're satisfied! Have a great trip!")
elif inquiry == "N":
    print("No problem! Let's make this plan work for you.")
else:
    print(input("Sorry. Please answer again in the correct format. Y/N "))
    