import json
from pathlib import Path
from difflib import SequenceMatcher

file_path = Path(__file__).with_name("data.json")

with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

items = data["items"]

print("University Helpdesk Chatbot")
print("Type 'exit' to stop.")

while True:
    user_question = input("\nYou: ").strip()

    if user_question.lower() == "exit":
        print("Goodbye!")
        break

    if not user_question:
        continue

    best_score = 0
    best_answer = None

    for item in items:
        saved_question = item["question"]
        score = SequenceMatcher(
            None,
            user_question.lower(),
            saved_question.lower()
        ).ratio()

        if score > best_score:
            best_score = score
            best_answer = item["answer"]

    if best_score >= 0.65:
        print("Chatbot:", best_answer)
    else:
        print("Chatbot: Sorry, I don't understand this question yet.")