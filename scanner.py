from parser import parse_eml
from rules.text_rules import analyze_text
from rules.url_rules import analyze_urls
from rules.header_rules import analyze_headers


def scan_eml_file(path):
    email = parse_eml(path)

    score = 0
    reasons = []

    t_s, t_r = analyze_text((email["subject"] or "") + " " + (email["body"] or ""))
    u_s, u_r = analyze_urls(email["body"] or "")
    h_s, h_r = analyze_headers(email["headers"] or "")

    score += t_s + u_s + h_s
    reasons += t_r + u_r + h_r

    score = min(score, 100)

    level = "LOW"
    if score >= 70:
        level = "HIGH"
    elif score >= 30:
        level = "MEDIUM"

    return {
        "file": path,
        "sender": email["sender"],
        "subject": email["subject"],
        "score": score,
        "level": level,
        "reasons": reasons
    }
