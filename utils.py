import random
import json

def select_category(categories):

    for index, category in enumerate(categories, start= 1):
    
        category_name = list(category.keys())[0]
        # category_name = category.keys()
        # print(type(category_name))
        print(f"[{index}] {category_name}")

    while True:
        try:
            choice = int(input("Enter the number of the category you want to play: "))
        except ValueError:
            print("Invalid value! Please enter a valid number.")
            continue

        if 1 <= choice <= len(categories):

            index = choice - 1
            
            return list(categories[index].values())[0]
        else:
            print(f"Invalid option! Please choose a number between 1 and {len(categories)}.")
            continue

def quiz(questions):

    score = 0

    copy_questions = list(questions)
    random.shuffle(copy_questions)

    copy_questions = copy_questions[:5]

    for index, question in enumerate(copy_questions, start=1):

        print("--------------------")
        print(f"Question {index}")
        print("--------------------")
        print(question['question'])

        copy_options = list(question['options'])
        random.shuffle(copy_options)
        for index, option in enumerate(copy_options, start= 1):

            print(f"[{index}] {option}")
        while True:
            try:
                choice = int(input("Pick an option: "))
            except ValueError:
                print("Invalid value! Please enter a valid number.")
                continue

            if 1 <= choice <= len(question['options']):

                index = choice - 1

                selected_choice = copy_options[index]
                break
            else:
                print("Invalid option! Please pick a valid option.")
                continue

        if selected_choice == question['answer']:

            score += 1
            
    return score, len(copy_questions)

def display_result(score, total_questions):

    print("--------------------")
    print("Quiz Complete!")
    print(f"Score: {score}/{total_questions}")
    print("--------------------")

    wrong = total_questions - score

    print(f"You got {score} correct and {wrong} incorrect.")

def load_questions(file_name):
    try:
        with open(file_name, "r") as file:
            questions = json.load(file)
        if not isinstance(questions, list):
            print("Invalid data format.")
            return []
        for category in questions:
            if not isinstance(category, dict):
                print("Invalid data format.")
                return []
            for value in category.values():
                if not isinstance(value, list):
                    print("Invalid data format.")
                    return []
                for question in value:
                    if not isinstance(question, dict):
                        print("Invalid data format.")
                        return []
        return questions
    except FileNotFoundError:
        print("Questions file not found.")
        return []
    except json.JSONDecodeError:
        print("Invalid JSON data.")
        return []