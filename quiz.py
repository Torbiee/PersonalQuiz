# This is the main file for my Personal Quiz

questionList = [
    ("When is your birthday?(XX/XX/XXXX)", "08/20/2002"),
    ("Who is the cutest cat ever?", "Mozelle")
]

for question, correct_answer in questionList:
    answer = input(f"{question}? ")
    if answer == correct_answer:
        print("Oh wow, you're so right!")
    else:
        print(f"Dumbass, study up! The correct answer is {correct_answer!r}! Not {answer!r}!")