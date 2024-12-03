# Name: Aleemuddin Ather
# Date: 2024-11-27
# Description: This module challenges the player to escape a trap set by a trusted ally using problem-solving skills.

def escape_trap():
    """Navigate a series of choices to escape a trap."""
    print("You've been ambushed by someone you trusted!")
    print("You must escape the trap before security arrives.")
    
    choices = {
        "A": "Attempt to pick the lock.",
        "B": "Search for hidden tools.",
        "C": "Try to break the door down."
    }
    
    for key, value in choices.items():
        print(f"{key}: {value}")
    
    correct_choice = "B"
    user_choice = input("What do you do? (A/B/C): ").upper()
    
    if user_choice == correct_choice:
        print("You found a hidden crowbar and managed to escape!")
        return True
    else:
        print("Your attempt failed, and you were captured.")
        return False
