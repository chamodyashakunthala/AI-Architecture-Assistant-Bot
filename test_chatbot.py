from app.chatbot.chatbot_core import chatbot_response

print("AI Architecture Assistant — Local Test")
print("---------------------------------------")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye!")
        break

    reply = chatbot_response(user_input)
    print("Chatbot:", reply)
