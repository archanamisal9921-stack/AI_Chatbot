print("🤖 Chatbot is ready! Type 'exit' to stop.")

while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        print("Chatbot: Goodbye! 👋")
        break

    if "hello" in user_input or "hi" in user_input:
        print("Chatbot: Hello! How can I help you?")
    elif "name" in user_input:
        print("Chatbot: I am your Python Chatbot!")
    elif "bye" in user_input:
        print("Chatbot: Goodbye! Have a great day! 😊")
        break
    else:
        print("Chatbot: Sorry, I don't understand that.")
