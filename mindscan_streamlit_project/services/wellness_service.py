"""Wellness recommendations and resources based on risk and sentiment."""

# Recommendations by risk band
RECOMMENDATIONS = {
    "Low": [
        "Keep up your journaling habit – consistency helps maintain awareness.",
        "Consider a short walk or stretch to maintain your positive momentum.",
        "Stay connected with people who support you.",
    ],
    "Moderate": [
        "Take a short break – a 5-minute walk or deep breathing can help.",
        "Try to get adequate sleep tonight – rest supports emotional balance.",
        "Talk to someone you trust about how you're feeling.",
        "Consider journaling again tomorrow to track any changes.",
    ],
    "Elevated": [
        "Reach out to a trusted friend, family member, or counselor.",
        "Prioritize rest – sleep and downtime matter for emotional recovery.",
        "Do one small thing that usually helps you feel better today.",
        "If these feelings persist, consider speaking with a mental health professional.",
    ],
}

# Support resources (user can verify local numbers)
SUPPORT_RESOURCES = [
    {"name": "Vandrevala Foundation (India)", "value": "1860-2662-345 / 1800-2333-330", "url": "https://www.vandrevalafoundation.com/"},
    {"name": "iCall (India)", "value": "022-25521111", "url": "https://icall.psychology.tiss.edu/"},
    {"name": "National Suicide Prevention Lifeline (US)", "value": "988", "url": "https://988lifeline.org/"},
    {"name": "Crisis Text Line", "value": "Text HOME to 741741", "url": "https://www.crisistextline.org/"},
]


def get_recommendations(risk_band: str, sentiment_label: str) -> list[str]:
    """Return personalized recommendations based on risk band and sentiment."""
    base = RECOMMENDATIONS.get(risk_band, RECOMMENDATIONS["Moderate"])
    # Add sentiment-specific tip
    if sentiment_label == "Negative" and risk_band != "Low":
        base = base + ["Be gentle with yourself. Negative feelings can shift over time."]
    return base


def get_support_resources() -> list[dict]:
    """Return support resource links (shown when risk is Elevated)."""
    return SUPPORT_RESOURCES


def get_weekly_insight(entries: list, avg_sentiment: float, risk_band: str) -> str:
    """Generate a brief insight based on recent entries."""
    n = len(entries)
    if n == 0:
        return "Add journal entries to see personalized insights."

    if avg_sentiment > 0.2:
        return f"Your recent entries ({n}) show a positive trend. Journaling regularly can help maintain this balance."
    elif avg_sentiment < -0.3:
        return f"Your recent entries suggest some strain. Consider rest, talking to someone, or a small self-care step today."
    else:
        return f"You've journaled {n} time(s) recently. Mixed or neutral feelings are normal – keep tracking to notice patterns."
