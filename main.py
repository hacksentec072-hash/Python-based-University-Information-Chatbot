
print("University Helpdesk Chatbot")
print("Welcome! خوش آمدید!")
print("Type 'exit' to stop.")

while True:
    question = input("\nYou: ").lower().strip()

    if question == "exit":
        print("Chatbot: Goodbye! خدا حافظ!")
        break

    elif any(word in question for word in [
        "admission", "apply", "داخلہ", "داخلے"
    ]):
        print("Chatbot: Please contact the admission office.")
        print("داخلے کی معلومات کے لیے داخلہ دفتر سے رابطہ کریں۔")

    elif any(word in question for word in [
        "exam", "examination", "paper", "امتحان", "پرچہ"
    ]):
        print("Chatbot: Please contact the examination office.")
        print("امتحانی معلومات کے لیے امتحانی دفتر سے رابطہ کریں۔")

    elif any(word in question for word in [
        "it department", "computer lab", "آئی ٹی", "کمپیوٹر لیب"
    ]):
        print("Chatbot: Please contact the IT department.")

    else:
        print("Chatbot: Sorry, I don't understand yet.")
        print("معذرت، میں ابھی یہ سوال نہیں سمجھ سکا۔")
