# 🤖 Smart Trainers Chatbot (CLI)

A rule-based Command Line Interface (CLI) chatbot developed for **Smart Trainers**. This Python program automates responses to Frequently Asked Questions (FAQs) regarding internships, courses, and company details.

## 📋 Project Overview
This chatbot serves as a virtual assistant to help students and applicants get instant information about Smart Trainers' programs. It uses keyword matching logic to understand user queries and provide relevant answers.

**Developed by:** Inayat Ali  
**Language:** Python 3.x

## ✨ Key Features
* **Keyword Detection:** intelligently scans user input for keywords like "courses", "location", "registration", etc.
* **Whole Word Matching:** Implements a padding logic (the "Space Trick") to distinguish between similar words (e.g., ensuring "hey" doesn't match inside "they").
* **Text Preprocessing:** Automatically handles case sensitivity and removes punctuation for smoother interaction.
* **Unknown Question Logging:** Records questions that the bot cannot answer into a list, helping developers identify what new answers need to be added later.
* **Interactive Loop:** Runs continuously until the user types "bye".

## 🚀 How to Run
1. Ensure Python is installed on your system.
2. Clone this repository or download the file.
3. Run the script in your terminal:
   ```bash
   python main.py