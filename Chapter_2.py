# Name: Aleemuddin Ather
# Date: 2024-11-27
# Description: This module features a hacking mini-game where Alex attempts to breach the Corporation's system
# to uncover vital information.

import random

def hacking_mini_game():
    """Simulate a basic hacking mini-game."""
    print("You need to hack into the Corporation's surveillance system.")
    code = random.randint(1000, 9999)
    print("Guess the 4-digit security code to gain access.")
    
    attempts = 3
    while attempts > 0:
        guess = input("Enter a 4-digit code: ")
        
        if guess.isdigit() and int(guess) == code: 
            print("Access granted! You've retrieved critical information.")
            return True
        else:
            attempts -= 1
            print(f"Wrong code. {attempts} attempts left.")
    
    print("Access denied. You must find another way.")
    return False
