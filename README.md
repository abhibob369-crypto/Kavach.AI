# Kavach.AI 🛡️
<img width="1281" height="573" alt="Screenshot 2026-10-31 121549" src="https://github.com/user-attachments/assets/dced03cb-ee66-479a-aa53-307fe95e888f" />


**Cyber-Defense & Privacy Suite**  
10 tools in one place. Powered by Gemini.

Everyday threats like fake UPI receipts, phishing links, deepfakes, voice scams, leaked IDs, weak passwords, and WhatsApp rumours — all handled from a single dashboard.

Built with Streamlit + Google Gemini (with multi-API key rotation so it doesn’t die on quota).

---

## What it does

| Tool | What you can do |
|------|-----------------|
| **Phishing & Payment Threat Detector** | Paste suspicious text/URL or upload payment screenshot (PNG/JPG/PDF). Detects fake receipts, spoofed UPI, phishing intent |
| **ID Privacy Shield** | Upload Aadhaar / PAN / any document → AI finds sensitive info that should be redacted |
| **Voice Call Transcript Analyzer** | Paste call transcript → checks for AI scam / urgency patterns |
| **Legal Contract Auditor** | Paste contract clauses → highlights hidden traps and unfavourable terms |
| **Email Domain Security Checker** | Enter email → quick 3-point security posture of the provider |
| **Deepfake / AI Image Detector** | Upload image → checks for AI generation artifacts |
| **Code Vulnerability Scanner** | Paste code → finds security issues + short patched version |
| **Terminal / Bash Script Analyzer** | Paste script → checks for malware intent |
| **Fake News & WhatsApp Rumor Checker** | Paste viral message → Fact-check (True / False / Misleading) |
| **Smart Password Guard** | Test password strength + suggests quantum-safe passphrases |

---

## Tech Stack

- Streamlit (UI)
- Google Generative AI (Gemini 1.5 / 2.0 Flash)
- Multi-API key rotation (handles quota exhaustion gracefully)
- pdf2image + Pillow (PDF & image support)
- Runs easily on Google Colab or local

---

## How to run

### Option 1: Google Colab (easiest)

1. Open the notebook `Kavach_AI.ipynb`
2. Put your Gemini API keys in the `API_KEYS` list
3. Run all cells
4. Click the public link that appears

### Option 2: Local

```bash
pip install streamlit google-generativeai pillow pdf2image
# also need poppler-utils for PDF support
