# Phishing-Email-Scanner

A web-based tool that analyzes email content for phishing indicators 
using heuristic detection techniques.

## Features
- Scans email text for suspicious keywords, spoofed domains, and 
  urgency language patterns
- Python (Flask) backend with a clean browser-based UI
- Returns a risk score and breakdown of detected indicators

## Tech Stack
- Python · Flask
- HTML · CSS · JavaScript

## How It Works
1. User pastes email content into the web interface
2. Backend analyzes text against phishing indicator ruleset
3. Results returned with flagged indicators highlighted

## Detection Methods
[List what your app.py actually checks for — keywords, URL patterns, 
sender spoofing, etc.]

## Setup
pip install -r requirements.txt
python app.py

## MITRE ATT&CK
Addresses T1566 — Phishing detection and awareness
