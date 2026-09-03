import json
from pathlib import Path


def load_faqs():
    """Load FAQ data from the JSON knowledge base."""

    project_root = Path(__file__).resolve().parents[2]
    faq_file = project_root / "data" / "faqs.json"

    with open(faq_file, "r", encoding="utf-8") as file:
        return json.load(file)


def find_intent(user_message, faqs):
    """Find an intent based on keyword groups."""

    message = user_message.lower()

    slow_keywords = [
        "slow",
        "slower",
        "wifi slow",
        "connection slow"
    ]

    connection_keywords = [
        "connection",
        "connect",
        "can't connect",
        "cannot connect",
        "offline",
        "no internet"
    ]

    human_keywords = [
        "human",
        "agent",
        "real person",
        "person",
        "representative"
    ]

    if any(keyword in message for keyword in human_keywords):
        return "human_agent"

    if any(keyword in message for keyword in slow_keywords):
        return "slow_internet"

    if any(keyword in message for keyword in connection_keywords):
        return "internet_problem"

    if "internet" in message and "not working" in message:
        return "internet_problem"

    if "password" in message or "forgot password" in message:
        return "password_reset"

    if "payment" in message or "pay" in message:
        return "payment_problem"

    if "price" in message or "cost" in message or "pricing" in message:
        return "pricing"

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