from analysis.review_analyzer import analyze_review


def test_promotional_review_flagged():
    review = "Best product ever!!! Highly recommended!!!"
    result = analyze_review(review, 5)
    assert result["is_suspicious"] is True


def test_genuine_negative_review_not_flagged():
    review = "The product quality was disappointing and delivery was late."
    result = analyze_review(review, 2)
    assert result["is_suspicious"] is False


def test_neutral_review_not_flagged():
    review = "Product is okay, does the job but nothing special."
    result = analyze_review(review, 3)
    assert result["is_suspicious"] is False
