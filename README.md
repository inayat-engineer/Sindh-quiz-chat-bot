# Chat-Style Quiz Bot (Sindh Heritage Edition)

## Project Overview
This project is a **Chat-Style Quiz Bot** developed in Python. It is designed to act as an interactive assistant that conducts a conversation-style quiz with the user. The bot quizzes users on the rich history, geography, and culture of the Sindh province, Pakistan. 

This project was developed as part of an **Internship Task** to demonstrate proficiency in Python fundamentals, specifically file handling, functional programming, and user interaction.

## Internship Task Requirements
The project fulfills the following criteria set by the internship guidelines:
- **Functional Python:** Built using simple, clean functions and loops.
- **External Data Loading:** Questions are not hard-coded; they are loaded from an external `.txt` file for flexibility.
- **Chat-Style Interaction:** The bot uses friendly, conversational language instead of a plain interface.
- **Instant Feedback:** Users receive immediate verification of their answers.
- **Persistent Storage:** Quiz results (Score, Name, and Timestamp) are automatically saved to a history file.
- **Replayability:** Includes a "Play Again" feature that allows multiple attempts without restarting the script.

## Key Features
- **Dynamic Question Loading:** Easily add or remove questions by editing `questions.txt`.
- **Randomized Experience:** Questions are shuffled in every round to keep the quiz engaging.
- **Input Validation:** Ensures the user only enters valid options (A, B, C, or D).
- **Time Tracking:** Displays the exact date and time of the attempt on the screen and logs it in the history file.

## Technologies Used
- **Python 3.x**
- **Modules:** `os`, `random`, `datetime`

## File Structure
- `quiz_chatbot.py`: The main Python script containing the logic.
- `questions.txt`: A text file containing the quiz data (Questions, Options, and Answers).
- `quiz_history.txt`: A log file where the bot saves player scores and timestamps.

## Setup and Installation

### 1. Prepare the Questions File
Create a file named `questions.txt` in the same directory as the script. The data must follow this format:
`Question|Option A|Option B|Option C|Option D|CorrectLetter`

**Example:**
```text
Who was the British General that led the conquest of Sindh in 1843?|A) Sir John Shore|B) Sir Charles Napier|C) Lord Dalhousie|D) Sir Thomas Roe|B
```

### 2. Run the Program
Open your terminal or IDE (like PyCharm) and run the script:
```bash
python quiz_chatbot.py
```

## How to Play
1. The bot will greet you and ask for your **Name**.
2. It will present **30 complex questions** about Sindh.
3. Answer by typing **A, B, C, or D**.
4. After the last question, the bot will show your **total score** and the **current date/time**.
5. You can choose to play again or exit by typing `yes` or `no`.

## Conclusion
The Chat-Style Quiz Bot demonstrates how simple programming concepts like file I/O and loops can be combined to create a practical, real-world application. It serves as a strong foundation for building more advanced chatbots or educational tools in the future.