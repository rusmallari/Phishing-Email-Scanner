# Phishing Email Scanner

A modular, web-based phishing detection tool that analyzes `.eml` 
email files across three detection layers: text heuristics, URL 
analysis, and email authentication headers.

## Features
- **Text analysis** — detects urgency language, brand impersonation 
  (PayPal, Microsoft, IRS, Apple, Amazon), and excessive capitalization
- **URL analysis** — flags IP-based URLs, @ obfuscation tricks, risky 
  TLDs (.tk .xyz .ru .pw), excessive subdomains, and suspicious 
  domain keywords
- **Header analysis** — checks SPF, DKIM, and DMARC authentication 
  failures
- **Risk scoring** — weighted 0–100 score with LOW / MEDIUM / HIGH 
  classification and per-flag breakdown

## Tech Stack
Python · Flask · HTML · CSS · JavaScript

## Setup & Usage
pip install flask
python app.py

Then open http://127.0.0.1:5000 and upload any .eml file.

## MITRE ATT&CK
Addresses T1566.001 — Spearphishing Attachment detection
