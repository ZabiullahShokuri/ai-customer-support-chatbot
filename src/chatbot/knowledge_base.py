import json
from pathlib import Path


def load_faqs():
    """Load FAQ data from the JSON knowledge base."""

    project_root = Path(__file__).resolve().parents[2]
    faq_file = project_root / "data" / "faqs.json"

    with open(faq_file, "r", encoding="utf-8") as file:
        return json.load(file)