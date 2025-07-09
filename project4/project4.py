def chatbot():
    print("Welcome to TamizhanBot! Type 'exit' to quit.")
    while True:
        user = input("You: ").lower()
        if user == 'exit':
            break
        elif "course" in user:
            print("Bot: We offer courses in Python, Web Dev, AI, and more!")
        elif "contact" in user:
            print("Bot: Email us at contact@tamizhanskills.com")
        elif "internship" in user:
            print("Bot: Our RISE internship is 100% free and project-based!")
        else:
            print("Bot: Sorry, I don't understand that. Try asking about our courses or internships.")

chatbot()