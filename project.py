def ask_question(question, options, correct_index):
    """Presents a question with multiple-choice options and validates user input."""
    print(question)
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    while True:
        try:
            user_input = int(input("Enter your answer (1-4): "))
            if 1 <= user_input <= len(options):
                return user_input == correct_index
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    """Runs the quiz game."""
    questions = [
        ("Who developed python programming language?", ["A. Wick van Rossam", "B. Guido van Rossum", "C. niene stom", "D. Rasmus"], 2),
        ("Which of the following is correct extension of the python file?", ["A. .python", "B. .pl", "C. .py", "D. .p"], 3),
        ("Which of the following is used to define a block of code in python?", ["A. key", "B. indentation", "C. brackets", "D. all of the above"], 2)
    ]
    score = 0

    for question, options, correct_index in questions:
        if ask_question(question, options, correct_index):
            score += 1
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {options[correct_index - 1]}")

    print(f"You finished the quiz with a score of {score} out of {len(questions)}.")

if __name__ == "__main__":
    main()
