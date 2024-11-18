# This is the main file for my Personal Quiz

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


for question, alternatives in questionsPlural.items():
    correct_answer = alternatives[0]
    sorted_alternatives = sorted(alternatives)
    for label, alternative in enumerate(sorted_alternatives):
        print(f"    {label}) {alternative}")

    answer_label = int(input(f"{question} "))
    answer = sorted_alternatives[answer_label]
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}!")


