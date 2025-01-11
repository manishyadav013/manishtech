import random


questions = {
    "What is the capital of France?": (["Paris", "London", "Berlin", "Madrid"], "Paris"),
    "What is 2 + 2?": (["3", "4", "5", "6"], "4"),
    "Which planet is known as the Red Planet?": (["Earth", "Mars", "Jupiter", "Venus"], "Mars"),
}

def run_quiz():
    question_list = list(questions.keys())
    random.shuffle(question_list)
    score = 0

    for question in question_list:
        options, correct_answer = questions[question]
        print("\n" + question)
        
        random.shuffle(options)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        try:
            user_answer = int(input("\nYour answer (1-4): "))
            if options[user_answer - 1] == correct_answer:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is {correct_answer}.")
        except (ValueError, IndexError):
            print("Invalid input! Please enter a number between 1 and 4.")

    print(f"\nYour final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    print("Welcome to the Quiz!")
    run_quiz()
