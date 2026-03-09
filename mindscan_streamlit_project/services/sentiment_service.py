
from textblob import TextBlob

def analyze_journal_text(text):
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0.2:
        label = "Positive"
    elif polarity < -0.2:
        label = "Negative"
    else:
        label = "Neutral"

    return {"score": round(polarity,3), "label": label}
