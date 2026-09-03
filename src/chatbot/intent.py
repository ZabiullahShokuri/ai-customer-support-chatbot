def find_intent(user_message, faqs=None):
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