from textblob import TextBlob

POSITIVE_WORDS = [
    "amazing", "excellent", "perfect", "best", "awesome",
    "fantastic", "great", "love", "wonderful"
]


def analyze_review(review_text: str, rating: int) -> dict:
    blob = TextBlob(review_text)
    polarity = blob.sentiment.polarity
    text_lower = review_text.lower()
    words = text_lower.split()

    # Basic metrics
    review_length = len(words)
    exclamation_count = review_text.count("!")

    # Positive word density
    positive_hits = sum(word in POSITIVE_WORDS for word in words)
    positive_density = positive_hits / max(review_length, 1)

    # Behavioral signals
    signals = {
        # Very positive but very short reviews are risky
        "short_overly_positive": review_length < 12 and polarity > 0.6,

        # Too much positivity packed together feels unnatural
        "high_positive_density": positive_density > 0.25,

        # Excessive punctuation is common in spam
        "excessive_exclamations": exclamation_count >= 3,

        # 5-star rating with weak or generic content
        "rating_content_mismatch": rating == 5 and polarity < 0.4,
    }

    suspicion_score = sum(signals.values())
    is_suspicious = suspicion_score >= 2  # lower threshold, stronger signals

    return {
        "sentiment_score": round(polarity, 2),
        "review_length": review_length,
        "positive_density": round(positive_density, 2),
        "suspicion_score": suspicion_score,
        "signals": signals,
        "is_suspicious": is_suspicious,
    }
