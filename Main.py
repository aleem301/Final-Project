# main.py
# Name: Aleemuddin Ather
# Date: 2024-11-27
# Description: Main game script integrating all modules into a cohesive storyline.

from random import seed
from Chapter_1 import introduce_story, npc_interaction
from Chapter_2 import hacking_mini_game
from Chapter_3 import decode_file
from Chapter_4 import escape_trap
from Chapter_5 import final_mission

def main():
    """Main function to run the game."""
    seed()  # Set a seed for randomization consistency during playthroughs
    
    print("Welcome to the Sci-Fi Mystery Adventure Game!")
    introduce_story()
    
    print("\n--- CHAPTER 1: NPC Interaction ---")
    npc_interaction()
    
    print("\n--- CHAPTER 2: Hacking Mini-Game ---")
    if not hacking_mini_game():
        print("Mission failed. Try again next time.")
        return
    
    print("\n--- CHAPTER 3: Decoding Puzzle ---")
    if not decode_file():
        print("Mission failed. Try again next time.")
        return
    
    print("\n--- CHAPTER 4: Escape the Trap ---")
    if not escape_trap():
        print("Mission failed. Try again next time.")
        return
    
    print("\n--- FINAL CHAPTER: Confrontation ---")
    final_mission()

    print("\nThank you for playing! Stay tuned for future updates.")
    print("Game developed by Aleemuddin Ather.")

if __name__ == "__main__":
    main()
