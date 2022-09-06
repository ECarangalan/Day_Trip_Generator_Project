
# (5 points): store my destinations, restaurants, mode of transportation, and entertainment in their own separate Lists. 
# (5 points): store my final day trip selections in a Dictionary, with a unique key value pair for each piece of my day trip. 
# Start coding the program first by going from the top of the user stories and working down. Decide how you will:
# Store the trip options for 
# destinations, restaurants, transportation, and entertainment each in their own List 
# (this would be good to place at the top of the file)
# Set up a Dictionary to store each randomly selected option.

destinations = ["River", "Beach", "Amuesment Park", "Park"]
restaurants = ["Yokozuna", "BurnCo BBQ", "The Whole Bowl", "Screen Door"]
mode_of_transportation = ["Bike", "Car", "Skate", "Bus", "Train"]
entertainment = ["Movie", "Concert", "Picnic", "Arcade"]

final_day_trip_selections = { 
   "destination" : destinations,
   "restaurant" : restaurants,
   "mot" : mode_of_transportation, 
   "entertainment" : entertainment}


import random

def random_destination_generator():
    final_day_trip_selections["destination"] = random.choice(destinations)
    random_destination = final_day_trip_selections["destination"]
    print(random_destination)

# random_destination_generator() 

def random_restaurant_generator() :
    final_day_trip_selections["restaurant"] = random.choice(restaurants)
    random_restaurant = final_day_trip_selections["restaurant"]
    print(random_restaurant)

# random_restaurant_generator()

def random_mot_generator() :
    final_day_trip_selections["mot"] = random.choice(mode_of_transportation)
    random_mot = final_day_trip_selections["mot"]
    print(random_mot)

# random_mot_generator()

def random_entertainment_generator() :
    final_day_trip_selections["entertainment"] = random.choice(entertainment)
    random_entertainment = final_day_trip_selections["entertainment"]
    print(random_entertainment)

# random_entertainment_generator()

def change_question() :
    change_prompt = (input("What part of your Day Trip would you like to change? (Destination, Restaurant, Mode of Transportation, Entertainment"))
    if change_prompt == "Destination" :
        change_destination()
    elif change_prompt == "Restaurant" :
        change_restaurant()
    elif change_prompt == "Mode of Transportation" :
        change_mot()
    elif change_prompt == "Entertainment" :
        change_entertainment()
    else:
        print("Invalid Selection! Try Again.")
        change_question()

def change_destination() :
    random_destination_generator()
    print(final_day_trip_selections)
    satisfaction_question = input("Accept Day Trip? (Yes/No)")
    if satisfaction_question == "Yes" :
        print("Woohoo! Enjoy your Day Trip!")
    elif satisfaction_question == "No" :
        change_question()

def change_restaurant() :
    random_restaurant_generator()
    print(final_day_trip_selections)
    satisfaction_question = input("Accept Day Trip? (Yes/No)")
    if satisfaction_question == "Yes" :
        print("Woohoo! Enjoy your Day Trip!")
    elif satisfaction_question == "No" :
        change_question()

def change_mot() :
    random_mot_generator()
    print(final_day_trip_selections)
    satisfaction_question = input("Accept Day Trip? (Yes/No)")
    if satisfaction_question == "Yes" :
        print("Woohoo! Enjoy your Day Trip!")
    elif satisfaction_question == "No" :
        change_question()

def change_entertainment() :
    random_entertainment_generator()
    print(final_day_trip_selections)
    satisfaction_question = input("Accept Day Trip? (Yes/No)")
    if satisfaction_question == "Yes" :
        print("Woohoo! Enjoy your Day Trip!")
    elif satisfaction_question == "No" :
        change_question()





def day_trip_generator() :
    random_destination_generator()
    random_restaurant_generator()
    random_mot_generator()
    random_entertainment_generator()
    satisfaction_question = input("Accept Day Trip? (Yes/No)")
    if satisfaction_question == "Yes" :
        print("Woohoo! Enjoy your Day Trip!")
    elif satisfaction_question == "No" :
        change_question()

            
day_trip_generator()



