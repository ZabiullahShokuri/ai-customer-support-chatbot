import json
from pathlib import Path


def load_faqs():
    """Load FAQ data from the JSON knowledge base."""

    project_root = Path(__file__).resolve().parents[2]
    faq_file = project_root / "data" / "faqs.json"

    with open(faq_file, "r", encoding="utf-8") as file:
        return json.load(file)


def find_intent(user_message, faqs):
    """Find an intent based on simple keyword matching."""

    message = user_message.lower()

    if "internet" in message and "not working" in message:
        return "internet_problem"

    if "internet" in message and "slow" in message:
        return "slow_internet"

    if "password" in message:
        return "password_reset"

    if "payment" in message:
        return "payment_problem"

    if "price" in message or "cost" in message:
        return "pricing"

    if "human" in message or "agent" in message:
        return "human_agent"

    return None


def main():
    faqs = load_faqs()

    print("AI Customer Support Chatbot")
    print("Type 'exit' to quit.\n")

    while True:
        user_message = input("You: ")

        if user_message.lower() == "exit":
            print("Bot: Goodbye!")
            break

        intent = find_intent(user_message, faqs)

        if intent:
            answer = faqs[intent]["answer"]
            print(f"Bot: {answer}\n")
        else:
            print("Bot: Sorry, I don't understand your question yet.\n")


if __name__ == "__main__":
    main()