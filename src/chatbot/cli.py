from .chatbot import create_chatbot, get_response


def main():
    """Run the chatbot in the command line."""

    faqs = create_chatbot()

    print("AI Customer Support Chatbot")
    print("Type 'exit' to quit.\n")

    while True:
        user_message = input("You: ")

        if user_message.lower() == "exit":
            print("Bot: Goodbye!")
            break

        response = get_response(user_message, faqs)
        print(f"Bot: {response}\n")


if __name__ == "__main__":
    main()