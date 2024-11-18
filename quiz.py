# This is the main file for my Personal Quiz
# A portion of this is from following the guide at https://realpython.com/python-quiz-application/


#import that allows the A, B, C, D options
from string import ascii_lowercase

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

# this sets the score to 0 so that you can start keeping score at 0
score = 0 

# for loop that grabs and numbers the questions
# it also labels the question answers in ABCD format and sorts them randomly
for num, (question, alternatives) in enumerate(questionsPlural.items(), start=1):
    print(f"\nQuestion {num}: ")
    print(f"{question}")
    correct_answer = alternatives[0]
    labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
    for label, alternative in labeled_alternatives.items():
        print(f"    {label}) {alternative}")

# This part grabs the user input and checks to make sure 
# the user input is valid
    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")

    # This part see's if the choice is correct or not and ouputs accordingly
    answer = labeled_alternatives[answer_label]
    if answer == correct_answer:
        # this adds to the score
        score += 1
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}!")


print(f"\nYou got {score} correct out of {num} questions")