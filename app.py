import streamlit as st
import google.generativeai as genai
import os
from PIL import Image
from pdf2image import convert_from_bytes

# ==========================================
# 🔑 API KEY CONFIGURATION (MULTI-KEY SETUP)
# ==========================================
API_KEYS = [
    "", # Paste your api key 1 is here
    "", # Paste your api key 2 is here
    "", # Paste your api key 3 is here
    ""  # Paste your api key 4 is here
]

def generate_safe_ai_response(content_input):
    last_exception = None
    for key in API_KEYS:
        if not key or "YOUR_" in key:
            continue
        try:
            genai.configure(api_key=key)
            model = genai.GenerativeModel("gemini-3.8-flash")
            return model.generate_content(content_input)
        except Exception as e:
            err = str(e)
            if "429" in err or "Quota" in err or "ResourceExhausted" in err:
                last_exception = e
                continue
            else:
                raise e
    raise Exception(f"All API Keys Quota Exhausted! Please wait 1 minute. Detail: {last_exception}")

# ==========================================
# 🎨 STREAMLIT UI & DASHBOARD SETUP
# ==========================================
st.set_page_config(page_title="Kavach.AI - Cyber Suite", layout="wide", page_icon="🛡️")

st.title("🛡️ Kavach.AI - Cyber-Defense & Privacy Suite")
st.markdown("**(Connected Engine: Gemini 2.5 Flash | 10-in-1 Real-Time Threat Protection)**")
st.divider()

tabs = st.tabs([
    "🎣 Phishing Scanner",
    "🪪 ID Privacy Shield",
    "🎙️ Voice Clone Detector",
    "⚖️ Legal Document Auditor",
    "🔓 Data Leak Checker",
    "🖼️ Deepfake Detector",
    "💻 Code Vulnerability Scanner",
    "📜 Suspicious Script Analyzer",
    "📰 Misinformation Verifier",
    "🔑 Password Guard"
])

# ==========================================
# 🚀 MODULE 1: Phishing & Payment Threat Detector (WITH PDF & IMAGE)
# ==========================================
with tabs[0]:
    st.subheader("🎣 Phishing & Payment Threat Detector")
    st.write("Analyze suspicious URLs, SMS, emails, or upload **Payment Screenshots/Invoices** (UPI/Bank) to check for fake receipts and scams.")

    threat_input = st.text_area("Paste suspicious text/URL here (Optional):", height=100)
    # Yahan 'pdf' add kar diya gaya hai
    uploaded_screenshot = st.file_uploader("Upload Payment Receipt (PNG, JPG, PDF) [Optional]", type=["png", "jpg", "jpeg", "pdf"])

    if st.button("Scan for Threat", key="phishing_btn"):
        if not threat_input and not uploaded_screenshot:
            st.warning("⚠️ Please provide either text or upload a receipt to scan!")
        else:
            with st.spinner("Analyzing threat pattern and document authenticity..."):
                try:
                    prompt_text = """
                    You are a Cybersecurity Expert. Analyze the input text/URL and the document image (if provided).
                    1. If a receipt/image is provided, check for fake payment spoofing (mismatched fonts, bad alignment, fake UPI format).
                    2. If text/URL is provided, check for phishing intent or scams.
                    Keep response strictly under 4 bullet points: Risk Score (%), Verdict, Red Flags, and Brief Advice.
                    """

                    content_to_send = [prompt_text]
                    if threat_input:
                        content_to_send.append(f"Input Text: {threat_input}")

                    if uploaded_screenshot is not None:
                        file_ext = uploaded_screenshot.name.split('.')[-1].lower()
                        # Agar file PDF hai, toh uske pehle page ko image me convert karo
                        if file_ext == 'pdf':
                            images = convert_from_bytes(uploaded_screenshot.read())
                            content_to_send.append(images[0])
                        else:
                            # Agar normal image hai, toh direct open karo
                            img = Image.open(uploaded_screenshot)
                            content_to_send.append(img)

                    response = generate_safe_ai_response(content_to_send)
                    st.success("Analysis Complete!")
                    st.info(response.text)
                except Exception as e:
                    st.error(f"Error during scan: {e}")

# ==========================================
# 🚀 MODULE 2 TO 10: Fast-Loading Modules
# ==========================================
with tabs[1]:
    st.subheader("🪪 ID Privacy Shield (Redaction)")
    id_image = st.file_uploader("Upload ID/Document", type=["png", "jpg", "jpeg", "pdf"], key="id_upload")
    if st.button("Scan & Redact ID"):
        if id_image:
            with st.spinner("Detecting sensitive data..."):
                file_ext = id_image.name.split('.')[-1].lower()
                if file_ext == 'pdf':
                    images = convert_from_bytes(id_image.read())
                    img = images[0]
                else:
                    img = Image.open(id_image)
                res = generate_safe_ai_response(["List sensitive information (Aadhaar, PAN, Card numbers) to REDACT. Keep it brief.", img])
                st.info(res.text)
        else:
            st.warning("Please upload a document.")

with tabs[2]:
    st.subheader("🎙️ Voice Call Transcript Analyzer")
    voice_text = st.text_area("Call Transcript:")
    if st.button("Analyze Call"):
        with st.spinner("Analyzing context..."):
            res = generate_safe_ai_response(f"Check this call transcript for AI scam/urgency patterns. Keep it short: {voice_text}")
            st.info(res.text)

with tabs[3]:
    st.subheader("⚖️ Legal Contract Auditor")
    contract_text = st.text_area("Paste contract clauses here:")
    if st.button("Audit Contract"):
        with st.spinner("Scanning for hidden traps..."):
            res = generate_safe_ai_response(f"Highlight unfavorable clauses or hidden traps in this contract. Keep it short: {contract_text}")
            st.info(res.text)

with tabs[4]:
    st.subheader("🔓 Email Domain Security Checker")
    email_input = st.text_input("Enter Email Address:")
    if st.button("Check Domain Security"):
        with st.spinner("Checking posture..."):
            res = generate_safe_ai_response(f"Give a brief 3-point security posture for the email provider of: {email_input}")
            st.info(res.text)

with tabs[5]:
    st.subheader("🖼️ Deepfake / AI Image Detector")
    df_image = st.file_uploader("Upload Image to check if it's AI generated", type=["png", "jpg", "jpeg"], key="df_img")
    if st.button("Detect AI Generation"):
        if df_image:
            with st.spinner("Analyzing pixels..."):
                img = Image.open(df_image)
                res = generate_safe_ai_response(["Analyze this image for AI generation artifacts. Keep response under 3 bullet points.", img])
                st.info(res.text)

with tabs[6]:
    st.subheader("💻 Code Vulnerability Scanner")
    code_input = st.text_area("Paste source code here:")
    if st.button("Audit Code"):
        with st.spinner("Finding bugs..."):
            res = generate_safe_ai_response(f"Find security vulnerabilities in this code and provide a short patched version: \n{code_input}")
            st.info(res.text)

with tabs[7]:
    st.subheader("📜 Terminal / Bash Script Analyzer")
    script_input = st.text_area("Paste command or script:")
    if st.button("Analyze Script"):
        with st.spinner("Checking for malware intent..."):
            res = generate_safe_ai_response(f"Does this script contain malware intent? Keep it short: {script_input}")
            st.info(res.text)

with tabs[8]:
    st.subheader("📰 Fake News & WhatsApp Rumor Checker")
    news_input = st.text_area("Paste viral message:")
    if st.button("Verify Fact"):
        with st.spinner("Fact-checking..."):
            res = generate_safe_ai_response(f"Fact-check this claim (True, False, or Misleading). Keep it under 3 bullet points: {news_input}")
            st.info(res.text)

with tabs[9]:
    st.subheader("🔑 Smart Password Guard")
    pwd_input = st.text_input("Enter a sample password to test:")
    if st.button("Check Strength"):
        with st.spinner("Calculating entropy..."):
            res = generate_safe_ai_response(f"Analyze the strength of this password and suggest 2 Quantum-Safe Passphrases. Keep it short: {pwd_input}")
            st.info(res.text)