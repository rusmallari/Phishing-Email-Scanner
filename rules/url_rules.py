import re
import urllib.parse


def analyze_urls(text):
    urls = re.findall(r'https?://[^\s]+', text)

    score = 0
    reasons = []

    for url in urls:
        domain = urllib.parse.urlparse(url).netloc.lower()

        if "@" in url or "%40" in url:
            score += 25
            reasons.append(f"URL obfuscation (@ trick): {url}")

        if domain.count(".") > 4:
            score += 10
            reasons.append(f"Excessive subdomains: {domain}")

        suspicious_keywords = ["login", "verify", "secure", "account", "update"]
        for kw in suspicious_keywords:
            if kw in domain:
                score += 5
                reasons.append(f"Suspicious keyword in domain: '{kw}' in {domain}")

        if re.match(r"\d+\.\d+\.\d+\.\d+", domain):
            score += 30
            reasons.append(f"IP-based URL detected (no domain): {domain}")

        risky_tlds = [".tk", ".xyz", ".top", ".cn", ".ru", ".pw"]
        for tld in risky_tlds:
            if domain.endswith(tld):
                score += 15
                reasons.append(f"Risky TLD detected: {domain}")

        if "-" in domain:
            score += 5
            reasons.append(f"Hyphenated domain (common in phishing): {domain}")

    return score, reasons
