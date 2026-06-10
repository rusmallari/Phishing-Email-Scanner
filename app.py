from flask import Flask, render_template, request, jsonify
import re
from urllib.parse import urlparse

app = Flask(__name__)

PHISHING_KEYWORDS = [
    "verify account","click here","urgent","immediately","suspended",
    "password reset","confirm identity","bank account","security alert","login now"
]

def analyze_email(email_text):
    score = 0
    reasons = []
    text = email_text.lower()

    for keyword in PHISHING_KEYWORDS:
        if keyword in text:
            score += 10
            reasons.append(f"Suspicious phrase detected: '{keyword}'")

    urls = re.findall(r'https?://[^\s]+', email_text)

    if urls:
        score += len(urls) * 5
        reasons.append(f"{len(urls)} URL(s) detected")

    for url in urls:
        domain = urlparse(url).netloc

        if re.match(r'^\d+\.\d+\.\d+\.\d+$', domain):
            score += 20
            reasons.append("IP address used instead of domain")

    score = min(score, 100)

    verdict = "LOW RISK"
    if score >= 70:
        verdict = "HIGH RISK"
    elif score >= 40:
        verdict = "MEDIUM RISK"

    return {"score": score, "verdict": verdict, "reasons": reasons}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    return jsonify(analyze_email(request.json['email']))

if __name__ == '__main__':
    app.run(debug=True)
