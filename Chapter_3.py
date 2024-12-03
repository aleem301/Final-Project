# Name: Aleemuddin Ather
# Date: 2024-11-27
# Description: This module involves solving a puzzle to decode an important file containing clues about Alex's sibling.

def decode_file():
    """Solve a puzzle to decode an important file."""
    print("You've found a corrupted file containing a clue about your sibling.")
    print("To access it, you must answer a series of questions.")
    
    questions = {
        "Q1": "What is 5 + 7? ",
        "Q2": "What is the capital of France? ",
        "Q3": "What programming language is this game written in? "
    }
    answers = {
        "Q1": "12",
        "Q2": "Paris",
        "Q3": "Python"
    }
    
    for question, correct_answer in questions.items():
        user_answer = input(question)
        if user_answer.strip().lower() != correct_answer.lower():
            print("Wrong answer! The file remains corrupted.")
            return False
    
    print("File decoded successfully! You’ve uncovered a major clue.")
    return True
