from src.chatbot.chatbot import load_faqs, find_intent


def test_load_faqs():
    faqs = load_faqs()

    assert "internet_problem" in faqs
    assert "slow_internet" in faqs
    assert "password_reset" in faqs


def test_internet_problem_intent():
    faqs = load_faqs()

    intent = find_intent(
        "My internet is not working",
        faqs
    )

    assert intent == "internet_problem"


def test_slow_internet_intent():
    faqs = load_faqs()

    intent = find_intent(
        "My internet is slow",
        faqs
    )

    assert intent == "slow_internet"


def test_password_reset_intent():
    faqs = load_faqs()

    intent = find_intent(
        "I forgot my password",
        faqs
    )

    assert intent == "password_reset"


def test_wifi_slow_intent():
    faqs = load_faqs()

    intent = find_intent(
        "The WiFi is extremely slow",
        faqs
    )

    assert intent == "slow_internet"


def test_connection_problem_intent():
    faqs = load_faqs()

    intent = find_intent(
        "My connection is terrible today",
        faqs
    )

    assert intent == "internet_problem"


def test_cannot_connect_intent():
    faqs = load_faqs()

    intent = find_intent(
        "I can't connect to the internet",
        faqs
    )

    assert intent == "internet_problem"


def test_real_person_intent():
    faqs = load_faqs()

    intent = find_intent(
        "Can I speak with a real person?",
        faqs
    )

    assert intent == "human_agent"