from .knowledge_base import load_faqs
from .intent import find_intent


def get_response(user_message, faqs):
    """Generate a response based on the detected intent."""

    intent = find_intent(user_message)

    if intent:
        return faqs[intent]["answer"]

    return "Sorry, I don't understand your question yet."


def create_chatbot():
    """Create and initialize the chatbot."""

    faqs = load_faqs()

    return faqs