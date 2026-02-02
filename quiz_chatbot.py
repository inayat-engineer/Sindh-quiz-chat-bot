import datetime
import os
import random

# Function for loading questions from txt file

def load_questions(filename):

    #Reads questions from a text file and returns them as a list.

    questions_list = []

    if not os.path.exists(filename):

        return []

    with open(filename, 'r', encoding='utf-8') as file:

        for line in file:

            # splitting by the pipe character '|'
            data = line.strip().split('|')

            if len(data) == 6:

                question_dict = {
                    "question": data[0],
                    "options": data[1:5],
                    "correct": data[5].upper()
                }
                questions_list.append(question_dict)
    return questions_list

# Function for saving score to history file

# Added 'timestamp' as a parameter to ensure screen and file match

def save_score_to_file(name, score, total, timestamp):

    #Saves the result with the provided date and time in quiz_history.txt.

    with open("quiz_history.txt", "a", encoding='utf-8') as file:

        file.write(f"[{timestamp}] Player: {name} | Score: {score}/{total}\n")

# Function for starting the quiz

def start_quiz():

    # Loading the data
    all_questions = load_questions("questions.txt")

    if not all_questions:
        print("Quiz Bot: Oops! I couldn't load the questions. Please check questions.txt.")
        return

    # Chat-style greeting


    print("Quiz Bot: Hello! I am your Sindh Heritage Assistant.")
    print("Quiz Bot: I'm here to have a conversation about our rich history.")


    user_name = input("Quiz bot: First, may I know your name? ")

    print(f"Quiz bot: Welcome, {user_name}! Let's start the quiz.\n")

    while True:

        # Shuffling questions to make it interactive and unique each time

        random.shuffle(all_questions)

        score = 0

        total_questions = len(all_questions)

        for i, q in enumerate(all_questions):

            print(f"Quiz bot: Question {i + 1}: {q['question']}")

            for opt in q['options']:

                print(f"     {opt}")

            user_answer = ""

            while user_answer not in ['A', 'B', 'C', 'D']:

                user_answer = input("Your answer (A, B, C, or D): ").strip().upper()

                if user_answer not in ['A', 'B', 'C', 'D']:

                    print("Quiz bot: Please just type A, B, C, or D.")

            # Instant Feedback
            if user_answer == q['correct']:
                print("Quiz bot: Fantastic! That is the correct answer. ✨")
                score += 1
            else:
                print(f"Quiz bot: Oh, that's not quite right. The correct answer was {q['correct']}. 📚")
            print("-" * 40)


        #  Capturing current date and time

        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Display the time on screen along with results

        print(f"Quiz bot: We've finished the quiz, {user_name}!")

        print(f"Quiz bot: Attempt Date & Time: {current_time}") # showing time on screen

        print(f"Quiz bot: You correctly answered {score} out of {total_questions} questions.")

        #  Pass the same timestamp to the save function

        save_score_to_file(user_name, score, total_questions, current_time)

        print("Quiz bot: I've successfully saved your progress in my history file.")

        # Playing again option
        choice = input("\nQuiz bot: Would you like to play another round? (yes/no): ").lower().strip()

        if choice != 'yes':

            print(f"Quiz bot: Allah Hafiz, {user_name}! It was great talking to you. Have a nice day!")
            break

        print("\nQuiz bot: Wonderful! Let's refresh the questions and start again.\n")

# main function calling
if __name__ == "__main__":
    start_quiz()