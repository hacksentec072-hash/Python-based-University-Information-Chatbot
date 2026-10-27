# University Helpdesk Chatbot Using Python

## Project Overview

The University Helpdesk Chatbot is a Python-based application designed to help students quickly find answers to frequently asked university-related questions. It provides information on common topics such as admissions, examinations, fee payments, scholarships, student ID cards, and university departments.

The system uses predefined questions and answers stored in a JSON file. It compares a student's question with stored questions using Python's built-in `difflib` module to identify a suitable response based on text similarity. If no sufficiently similar question is found, the chatbot displays a message asking the student to try another question.

The project aims to make common university information easier to access, reduce repetitive inquiries, and provide a simple, user-friendly way for students to obtain basic information.

## Features

- Provides answers to common university-related questions.
- Compares user questions with predefined questions using text similarity.
- Displays a fallback message when no suitable match is found.
- Stores predefined questions and answers in a JSON file.
- Runs locally on a computer without requiring an internet connection.
- Can be improved by adding more questions and answers.

## Technologies Used

- **Python:** Used to develop the chatbot's functionality.
- **JSON:** Used to store predefined questions and answers.
- **difflib:** Python's built-in module for comparing text similarity.
- **Visual Studio Code:** Used to write, edit, and run the code.
- **Git and GitHub:** Used to manage and store the project's source code online.

## Project Files

- `main.py` — Contains the original chatbot program.
- `nlp_chatbot.py` — Contains the text similarity-based chatbot.
- `data.json` — Stores the predefined questions and answers.

## How to Run

### Requirements
- Python installed on your computer.
- The project files downloaded to your computer.

### Instructions

1. Download or clone this repository.
2. Open the project folder in a terminal or Command Prompt.
3. Run the following command:

   ```bash
   python nlp_chatbot.py
   ```

4. Type a question in English.
5. Read the chatbot's response.
6. Type `exit` to close the chatbot.

## Current Limitations

- The chatbot answers questions using predefined information.
- It may not understand questions phrased in unfamiliar ways.
- Its responses depend on the questions and answers stored in `data.json`.
- It does not currently use a trained machine-learning model.

## Future Improvements

- Add more frequently asked university questions.
- Improve question matching and response accuracy.
- Test the chatbot with different question formats.
- Update answers using verified university information.
- Improve the chatbot based on testing and supervisor feedback.

## Project Status

This project is a student Final Year Project (FYP) prototype. It will be tested and improved as development continues.

## GitHub Repository

https://github.com/hacksentec072-hash/UniversityHelpdeskChatbot
