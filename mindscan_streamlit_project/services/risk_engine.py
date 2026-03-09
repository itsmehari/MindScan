
def calculate_text_risk(sentiment):
    score = sentiment["score"]

    if score <= -0.5:
        return "Elevated"
    elif score <= -0.2:
        return "Moderate"
    return "Low"
