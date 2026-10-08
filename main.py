# from utils import (
#     select_category, 
#     quiz, 
#     display_result, 
#     load_questions
# )
from utils import *

file_name = "questions.json"

categories = load_questions(file_name)

if not categories:
    exit()

print("Welcome to Game Trivia!")

def play_game(categories):

    while True:

        questions = select_category(categories)

        score, total_questions = quiz(questions)

        display_result(score, total_questions)

        while True:

            play_again = input("Do you want to play again? (y/n): ").lower().strip()

            if play_again not in ("y", "n"):
                print("Invalid input! Please enter (y/n).")
                continue
            else:
                break
            
        if play_again == "n":
            break

play_game(categories)
