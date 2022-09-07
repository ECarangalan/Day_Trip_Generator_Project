
# (5 points): store my destinations, restaurants, mode of transportation, and entertainment in their own separate Lists. 
# (5 points): store my final day trip selections in a Dictionary, with a unique key value pair for each piece of my day trip. 
# Start coding the program first by going from the top of the user stories and working down. Decide how you will:
# Store the trip options for 
# destinations, restaurants, transportation, and entertainment each in their own List 
# (this would be good to place at the top of the file)
# Set up a Dictionary to store each randomly selected option.

destinations = ["River", "Beach", "Amuesment Park", "Park", "Skate Park", "Mountain"]
restaurants = ["Yokozuna", "BurnCo BBQ", "The Whole Bowl", "Screen Door", "Fried Egg I'm in Love", "Harlow"]
mode_of_transportation = ["Bike", "Car", "Bus", "Train", "Walk"]
entertainment = ["Movie", "Concert", "Picnic", "Arcade", "Museum", "Art Crawl", "Berry Picking"]

final_day_trip_selections = { 
   "dest" : destinations,
   "rest" : restaurants,
   "motr" : mode_of_transportation, 
   "ent" : entertainment}

final_day_trip_confirm = {
    "destination" : final_day_trip_selections["dest"],
    "restaurant" : final_day_trip_selections["rest"],
    "mot" : final_day_trip_selections["motr"],
    "entertainment" : final_day_trip_selections["ent"]
}

from multiprocessing import Value
import random


# def change_question() :
#     change_prompt = (input("What part of your Day Trip would you like to change? (Destination, Restaurant, Mode of Transportation, Entertainment"))
#     if change_prompt == "Destination" :
#         change_destination()
#     elif change_prompt == "Restaurant" :
#         change_restaurant()
#     elif change_prompt == "Mode of Transportation" :
#         change_mot()
#     elif change_prompt == "Entertainment" :
#         change_entertainment()
#     else:
#         print("Invalid Selection! Try Again.")
#         change_question()

def change_destination() :
    random_destination_generator()

def change_restaurant() :
    random_restaurant_generator()
    

def change_mot() :
    random_mot_generator()
    

def change_entertainment() :
    random_entertainment_generator()
    


def random_destination_generator():
    final_day_trip_selections["dest"] = random.choice(destinations)
    random_destination = final_day_trip_selections["dest"]
    dest_result = (input(f"Would you like to go to the {random_destination}? (Y/N)"))
    if dest_result == "Y" :
        print(f"To the {random_destination} you go!")
        print("------------------------")
        print(" ")
        return  random_destination
        # random_restaurant_generator()
    elif dest_result == "N" :
        change_destination()
    else:
        print("Invalid input! Try again!")
        change_destination()

# random_destination_generator() 

def random_restaurant_generator() :
    final_day_trip_selections["rest"] = random.choice(restaurants)
    random_restaurant = final_day_trip_selections["rest"]
    rest_result = (input(f"Would you like to eat at {random_restaurant}? (Y/N)"))
    if rest_result == "Y" :
        print(f"{random_restaurant} it is!")
        print("------------------------")
        print(" ")
        return random_restaurant
        # random_mot_generator()
    elif rest_result == "N" :
        change_restaurant()
    else:
        print("Invalid input! Try again!")
        change_restaurant()



# random_restaurant_generator()

def random_mot_generator() :
    final_day_trip_selections["motr"] = random.choice(mode_of_transportation)
    random_mot = final_day_trip_selections["motr"]
    mot_result = (input(f"Does taking a {random_mot} for transportation work for you? (Y/N)"))
    if mot_result == "Y" :
        print(f"A {random_mot} you shall take!")
        print("------------------------")
        print(" ")
        return random_mot
        # random_entertainment_generator()
    elif mot_result == "N" :
        change_mot()
    else:
        print("Invalid input! Try again!")
        change_mot()



# random_mot_generator()

def random_entertainment_generator() :
    final_day_trip_selections["ent"] = random.choice(entertainment)
    random_entertainment = final_day_trip_selections["ent"]
    ent_result = (input(f"How does a(n) {random_entertainment} sound? (Y/N)"))
    if ent_result == "Y" :
        print(f"Enjoy your {random_entertainment}!")
        print("------------------------")
        print(" ")
        return random_entertainment
    elif ent_result == "N" :
        change_entertainment()
    else:
        print("Invalid input! Try again!")
        change_entertainment()

# random_entertainment_generator()


def change_question() :
    change_prompt = (input("What part of your Day Trip would you like to change? (Destination, Restaurant, Mode of Transportation, Entertainment: "))
    seleciton_changed = False
    while seleciton_changed == False :
        if change_prompt == "Destination" :
            change_destination()
            seleciton_changed = True
        elif change_prompt == "Restaurant" :
            change_restaurant()
            seleciton_changed = True
        elif change_prompt == "Mode of Transportation" :
            change_mot()
            seleciton_changed = True
        elif change_prompt == "Entertainment" :
            change_entertainment()
            seleciton_changed = True
        else:
            print("Invalid Selection! Try Again.")
            change_question()

# def change_destination() :
#     random_destination_generator()
#     print(final_day_trip_selections)
#     satisfaction_question = input("Accept Day Trip? (Y/N)")
#     if satisfaction_question == "Y" :
#         print("Woohoo! Enjoy your Day Trip!")
#     elif satisfaction_question == "N" :
#         change_question()

# def change_restaurant() :
#     random_restaurant_generator()
#     print(final_day_trip_selections)
#     satisfaction_question = input("Accept Day Trip? (Yes/No)")
#     if satisfaction_question == "Yes" :
#         print("Woohoo! Enjoy your Day Trip!")
#     elif satisfaction_question == "No" :
#         change_question()

# def change_mot() :
#     random_mot_generator()
#     print(final_day_trip_selections)
#     satisfaction_question = input("Accept Day Trip? (Yes/No)")
#     if satisfaction_question == "Yes" :
#         print("Woohoo! Enjoy your Day Trip!")
#     elif satisfaction_question == "No" :
#         change_question()

# def change_entertainment() :
#     random_entertainment_generator()
#     print(final_day_trip_selections)
#     satisfaction_question = input("Accept Day Trip? (Yes/No)")
#     if satisfaction_question == "Yes" :
#         print("Woohoo! Enjoy your Day Trip!")
#     elif satisfaction_question == "No" :
#         change_question()



def day_trip_generator() :
    random_destination_generator()
    random_restaurant_generator()
    random_mot_generator()
    random_entertainment_generator()
    final_day_trip_confirm = {
    "destination" : final_day_trip_selections["dest"],
    "restaurant" : final_day_trip_selections["rest"],
    "mot" : final_day_trip_selections["motr"],
    "entertainment" : final_day_trip_selections["ent"]
}
    print("------------------------")
    print("Below is the trip you said yes to!")
    print("------------------------")
    for key,value in final_day_trip_confirm.items() :
        print(f"     The {key} you said yes to is: {value} ")
        final_day_trip_selections["dest"]
        final_day_trip_selections["rest"]
        final_day_trip_selections["motr"]
        final_day_trip_selections["ent"]
    # satisfaction_question = (input(f"Are you sure you want to go to the {final_day_trip_confirm['destination']}, eat at {final_day_trip_confirm['restaurant']}, then take a {final_day_trip_confirm['mot']}, to a(n) {final_day_trip_confirm['entertainment']} for your Day Trip? (Y/N)"))
    user_satisfied = False
    print("----------------------")

    while user_satisfied == False :
        final_day_trip_confirm = {
    "destination" : final_day_trip_selections["dest"],
    "restaurant" : final_day_trip_selections["rest"],
    "mot" : final_day_trip_selections["motr"],
    "entertainment" : final_day_trip_selections["ent"]}

        satisfaction_question = (input(f"Are you sure you want to go to the {final_day_trip_confirm['destination']}, eat at {final_day_trip_confirm['restaurant']}, then take a {final_day_trip_confirm['mot']}, to a(n) {final_day_trip_confirm['entertainment']} for your Day Trip? (Y/N)"))        
        if satisfaction_question == "Y" :
            print("------------------------")
            print("Woohoo! Enjoy your Day Trip!")
            user_satisfied = True
            # satisfaction_question = (input(f"Are you sure you want to go to the {final_day_trip_confirm['destination']}, eat at {final_day_trip_confirm['restaurant']}, then take a {final_day_trip_confirm['mot']}, to a(n) {final_day_trip_confirm['entertainment']} for your Day Trip? (Y/N)"))
            break
        elif satisfaction_question == "N" :
            print("------------------------")
            print(" ")
            change_question()
        else:
            print("Invalid response. Try again!")
            change_question()

print("----------------------")
print(" ")
print("Welcome to the Day Trip Generator!")
print(" ")
print("----------------------")
print("Let's get started!")
print(" ")
            
day_trip_generator()



