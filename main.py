# main.py

from data import quiz


def run_quiz():
    score = 0
    total_questions = len(quiz)

    for key in quiz:
        # Retrieve the question and answer
        question = quiz[key]["question"]
        correct_answer = quiz[key]["answer"]

        # Print the question and get the user's answer
        user_answer = input(f"{question} ").strip()

        # Check if the user's answer is correct (case-insensitive)
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")

        # Display the current score
        print(f"Current Score: {score}/{total_questions}")

    # Display final results
    print("\nQuiz Complete!")
    print(f"Total Correct Answers: {score}/{total_questions}")
    percentage = (score / total_questions) * 100
    print(f"Percentage Correct: {percentage:.2f}%")


if __name__ == "__main__":
    run_quiz()
