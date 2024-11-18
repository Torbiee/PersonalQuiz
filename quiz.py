# This is the main file for my Personal Quiz
# A portion of this is from following the guide at https://realpython.com/python-quiz-application/

# imports randomness to the file
import random
# import that allows the A, B, C, D options
from string import ascii_lowercase

num_questions_per_quiz = 5
# questions put in a dictionary and the answers in a list?
# double check that though
questionsPlural = {
    "When is your birthday?(XX/XX/XXXX)": [
        "08/20/2002", "02/18/2002", "10/12/2005", "04/16/1975"
        ],
    "Who is the cutest cat ever?": [
        "Mozelle", "Skippy", "Jimbo", "Bro"
    ],
    "What does Will get at Sushi mon?": [
        "Udon", "Chicken Teryiaki", "Miso Soup", "A Big Block of Cheese"
    ],
    "What is the best fallout game?": [
        "Fallout 4", "Fallout 3", "Fallout New Vegas", "Fallout 76"
    ],

}

# this function deals with the number of questions and the questions overall
def prepare_questions(questions, num_questions): 
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)

# this function displays the question and answer choices, 
# using ascii_lowercase to add the ABCD and then labels them accordingly
# then it checks to make sure user input is valid and collects the 
# user input
# to help better understand, this function represents the user's answer when
# called elsewhere 
def get_answer(question, alternatives):
    print(f"{question}")
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    for label, alternative in labeled_alternatives.items():
        print(f"    {label}) {alternative}")

    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please pick either {', '.join(labeled_alternatives)}")

    return labeled_alternatives[answer_label]


# this function makes the choices random, 
# collects the user input to check and see if it is right, and displays
# an output accordingly
def ask_question(question, alternatives):
    correct_answer = alternatives[0]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    
    answer = get_answer(question, ordered_alternatives)
    if answer == correct_answer:
        print("Correct!!")
        return True # or you could put 1, True = 1, False = 0
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
        return False


# def run_quiz():
