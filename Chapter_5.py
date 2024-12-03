# Name: Aleemuddin Ather
# Date: 2024-11-27
# Description: This module represents the climactic final mission where the player decides how to confront the Corporation.

def final_mission():
    """Execute the final mission and determine the game's outcome."""
    print("You've reached the Corporation's headquarters.")
    print("It's time to confront the CEO and uncover the truth.")
    
    choices = {
        "1": "Confront the CEO directly.",
        "2": "Sneak into the data center to expose their secrets.",
        "3": "Plant a virus to take down their systems."
    }
    
    for key, value in choices.items():
        print(f"{key}: {value}")
    
    user_choice = input("What do you choose to do? (1/2/3): ")
    
    if user_choice == "1":
        print("You confronted the CEO, but they were prepared. The mission failed.")
    elif user_choice == "2":
        print("You snuck into the data center and exposed the Corporation's secrets! Victory!")
    elif user_choice == "3":
        print("You planted a virus and crippled the Corporation’s operations. The city is free!")
    else:
        print("Invalid choice. The mission failed.")
