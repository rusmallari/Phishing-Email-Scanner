def analyze_headers(headers):
    score = 0
    reasons = []

    h = headers.lower()

    if "spf=fail" in h:
        score += 25
        reasons.append("SPF authentication failed (sender domain mismatch)")

    if "dkim=fail" in h:
        score += 25
        reasons.append("DKIM signature invalid (email may be tampered)")

    if "dmarc=fail" in h:
        score += 25
        reasons.append("DMARC policy failure (unauthorized sender)")

    if "spf=softfail" in h:
        score += 10
        reasons.append("SPF soft fail detected")

    return score, reasons
