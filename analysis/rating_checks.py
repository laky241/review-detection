from textblob import TextBlob

def sentiment_mismatch(text: str, rating: int) -> bool:
    """
    Flags reviews where sentiment and rating don't align.
    Example: very positive text but low rating.
    """
    sentiment = TextBlob(text).sentiment.polarity

    if sentiment > 0.5 and rating <= 2:
        return True
    if sentiment < -0.5 and rating >= 4:
        return True

    return False
