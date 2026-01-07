import re

def repeated_words_score(text: str) -> int:
    """
    Detects excessive repetition of the same word.
    Fake reviews often repeat words unnaturally.
    """
    words = text.lower().split()
    repeats = len(words) - len(set(words))
    return repeats


def excessive_punctuation(text: str) -> bool:
    """
    Flags reviews with too many exclamation marks.
    """
    return text.count("!") >= 3


def promotional_language(text: str) -> bool:
    """
    Detects common promotional phrases seen in fake reviews.
    """
    promo_phrases = [
        "highly recommended",
        "best product ever",
        "must buy",
        "worth every penny"
    ]
    text_lower = text.lower()
    return any(phrase in text_lower for phrase in promo_phrases)
