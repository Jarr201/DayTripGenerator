import random

destination = ["Bahamas", "Tokyo", "New York", "Florida"]
restuarant = ["fast food place", "buffet", "diner", "bar"]
transportation = ["train", "airplane", "car", "cruise ship"]
entertainment  = ["nature walk", "shopping spree", "city tour", "beach visit"]

intro = input("Hello and Welcome to your trip planner! Lets get you started!")
print(intro)

trip_dest = random.choice(destination)
trip_rest = random.choice(restuarant)
trip_trans = random.choice(transportation)
trip_enter = random.choice(entertainment)


full_trip = f"You'll be visiting {trip_dest} via {trip_trans}. During your trip, you should eat at a {trip_rest} and go on a {trip_enter} while you're out!"
print(full_trip)