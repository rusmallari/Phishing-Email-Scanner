# 🛡️ Phishing Email Scanner

A SOC-style tool for analyzing raw `.eml` email files and producing a weighted phishing risk score, with a full breakdown of every red flag detected.

**Live demo:** [phishing-email-scanner.onrender.com](https://phishing-email-scanner.onrender.com)

> Note: hosted on Render's free tier — if the app has been idle, the first load may take 30–50 seconds to spin back up.

---

## Overview

Upload a `.eml` file (the raw export format produced by Gmail, Outlook, Apple Mail, etc.) and the scanner runs it through three independent detection layers, then combines the results into a single risk score from 0–100 with a plain-English breakdown of what triggered it.

---

## Detection Layers

### 1. Text & Language Analysis
Scans the subject and body for:
- Urgency and pressure language ("urgent," "immediately," "verify now," "action required")
- Brand impersonation keywords (PayPal, Microsoft, IRS, Apple, Amazon, Google, etc.)
- Excessive capitalization, a common spam/phishing signal

### 2. URL & Domain Analysis
Scans any links in the body for:
- The `@` obfuscation trick (hides the real destination domain)
- Excessive subdomains
- Suspicious keywords embedded in the domain itself (`login`, `verify`, `secure`, `account`, `update`)
- Raw IP addresses used instead of a domain name
- Risky top-level domains (`.tk`, `.xyz`, `.top`, `.cn`, `.ru`, `.pw`)
- Hyphenated domains (e.g. `paypal-secure-login.com`)

### 3. Header Forensics
Parses the email's existing `Authentication-Results` header to check whether the sending mail server's own SPF, DKIM, and DMARC checks passed or failed — surfacing sender spoofing and domain authentication failures without needing live DNS lookups.

---

## Scoring

Each layer contributes points independently. The combined score is capped at 100 and mapped to a risk tier:

| Score | Verdict |
|---|---|
| 0–29 | LOW |
| 30–69 | MEDIUM |
| 70–100 | HIGH |

---

## Tech Stack

- **Backend:** Python, Flask
- **Server:** Gunicorn
- **Frontend:** HTML, CSS, vanilla JavaScript
- **Email parsing:** Python's built-in `email` library (no external dependencies for parsing)

---

## Project Structure

```
Phishing-Email-Scanner/
├── app.py                  # Flask routes
├── scanner.py               # Orchestrates the three detection layers
├── parser.py                 # Parses raw .eml files into subject/sender/body/headers
├── rules/
│   ├── text_rules.py         # Layer 1: language heuristics
│   ├── url_rules.py          # Layer 2: URL/domain analysis
│   └── header_rules.py       # Layer 3: SPF/DKIM/DMARC forensics
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── requirements.txt
```

---

## Running It Locally

**1. Clone the repo**
```bash
git clone https://github.com/rusmallari/Phishing-Email-Scanner.git
cd Phishing-Email-Scanner
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
python app.py
```

**4. Open it in your browser**
```
http://127.0.0.1:5000
```

Drag and drop a `.eml` file onto the page, or click "Browse File" to select one. Results appear in real time — risk score, verdict, sender, subject, and every flag that was triggered.

---

## Testing It

Sample `.eml` files for testing can be found at:
- [Malware-Traffic-Analysis.net](https://www.malware-traffic-analysis.net/) — real, defanged phishing samples used widely in SOC training
- [rf-peixoto/phishing_pot](https://github.com/rf-peixoto/phishing_pot) — a maintained collection of phishing samples for detection tool development

> These are real captured phishing emails. The scanner only reads text and headers — it never visits any links — but avoid clicking any URLs inside the `.eml` files yourself.

---

## Screenshots

<img width="300" height="250" alt="Phishing-Email-LOW" src="https://github.com/user-attachments/assets/be5be5f1-4e44-4eb7-8d3f-262cc1592599" />
<img width="300" height="250" alt="Phishing-Email-MEDIUM" src="https://github.com/user-attachments/assets/a335bdc0-c2dd-430e-be64-67639799fef3" />
<img width="300" height="250" alt="Phishing-Email-HIGH" src="https://github.com/user-attachments/assets/0a72a5e9-3cf4-45b8-81fa-0b69d3908d47" />

---


## Disclaimer

This tool is for **educational and portfolio purposes**. It is a heuristic, rules-based scanner — not a production-grade email security product — and should not be relied on as a sole line of defense against phishing.

---

## License

Open source, available under the MIT License.
