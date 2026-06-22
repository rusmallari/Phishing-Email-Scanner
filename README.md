# 🛡️ Phishing Email Scanner

A fully offline, SOC-style phishing detection web app that analyzes `.eml` email files — no APIs, no external services, no copy-pasting email content.

## Features

- 📧 Drag & drop `.eml` file upload
- 🔗 URL analysis (IP-based URLs, obfuscation tricks, risky TLDs, suspicious keywords)
- 🧠 Phishing language detection (urgency patterns, brand impersonation)
- 📨 Email header authentication checks (SPF / DKIM / DMARC)
- 📊 Risk score (0–100) with LOW / MEDIUM / HIGH classification
- 🖥️ Clean dark-mode web UI
- 🔒 Fully offline — no data leaves your machine

## Project Structure

```
phishing-scanner-web/
│
├── app.py              # Flask backend
├── scanner.py          # Core scan engine
├── parser.py           # .eml file parser
├── requirements.txt
│
├── rules/
│   ├── text_rules.py   # Keyword & language analysis
│   ├── url_rules.py    # URL heuristics
│   └── header_rules.py # SPF/DKIM/DMARC checks
│
├── templates/
│   └── index.html      # Web UI
│
├── static/
│   └── style.css       # Styling
│
└── uploads/            # Scanned files stored here
```

## How to Run

**1. Install dependencies**
```bash
pip install -r requirements.txt
```

**2. Start the server**
```bash
python app.py
```

**3. Open your browser**
```
http://127.0.0.1:5000
```

**4. Export a `.eml` file from Gmail or Outlook and drop it into the UI.**

## How to Export a `.eml` File

- **Gmail**: Open email → three-dot menu → *Download message*
- **Outlook**: File → Save As → choose `.eml` format
- **Thunderbird**: Drag email to desktop

## Risk Levels

| Score | Level  | Meaning                          |
|-------|--------|----------------------------------|
| 0–29  | LOW    | Likely safe                      |
| 30–69 | MEDIUM | Suspicious — review carefully    |
| 70–100| HIGH   | Strong phishing indicators       |

## Tech Stack

- **Backend**: Python, Flask
- **Parsing**: Python standard library `email`
- **Frontend**: Vanilla HTML/CSS/JS

## About

Built as a portfolio cybersecurity project demonstrating SOC-style email triage tooling. Rule-based detection with modular architecture designed for future ML and threat feed integration.
