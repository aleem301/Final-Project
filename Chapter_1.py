# Name: Aleemuddin Ather
# Date: 2024-11-27
# Description: This module introduces the main character, Alex, and sets up the initial plot of the game. 
# The player interacts with an NPC to gather early clues about the missing sibling.

from random import shuffle

def introduce_story():
    """Introduce the main plot and character Alex."""
    print("Welcome to the game!")
    print("You play as Alex, a skilled hacker living in a city controlled by a mega-corporation.")
    print("Your sibling has gone missing, and it’s up to you to uncover the truth.")
    print("Your journey begins now.")

def npc_interaction():
    """Introduce an NPC for Alex to talk to."""
    responses = [
        "I saw someone matching your sibling's description last week.",
        "Be careful asking too many questions. The Corporation is watching.",
        "I don’t know anything. Leave me alone!"
    ]
    npc_names = ["Jordan", "Sam", "Taylor", "Jamie"]
    
    shuffle(npc_names)
    npc_name = npc_names[0]
    
    print(f"{npc_name}: Hey there, I'm {npc_name}.")
    answer = input("Do you want to talk to me? (y/n): ").lower()
    
    if answer == "y":
        shuffle(responses)
        print(f"{npc_name}: {responses[0]}")
    else:
        print(f"{npc_name}: Maybe next time.")
