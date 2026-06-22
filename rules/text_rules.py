import re


def analyze_text(text):
    score = 0
    reasons = []

    t = text.lower()

    patterns = [
        r"urgent",
        r"immediately",
        r"verify now",
        r"account.*suspend",
        r"action required",
        r"click here",
        r"confirm identity",
        r"security alert",
    ]

    for p in patterns:
        if re.search(p, t):
            score += 10
            reasons.append(f"Urgency/phishing language detected: '{p}'")

    trusted_brands = ["bank", "paypal", "microsoft", "irs", "apple", "amazon", "google"]
    for brand in trusted_brands:
        if brand in t:
            score += 10
            reasons.append(f"Possible brand impersonation: '{brand}'")

    caps = sum(1 for c in text if c.isupper())
    if len(text) > 0 and caps / len(text) > 0.3:
        score += 10
        reasons.append("Excessive capitalization detected")

    return score, reasons
