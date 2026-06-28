import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(page_title="ERPNext Lab Control Portal", layout="wide")

st.title("🎓 ERPNext Lab Control Portal")
st.write("Welcome to the cloud-based ERPNext student lab. Authorize via the sidebar to access your ERPNext environment.")

# Sidebar Login & Settings
st.sidebar.header("🔑 Authentication & Control")
username = st.sidebar.text_input("Student Username")
password = st.sidebar.text_input("Password", type="password")

# API Key for Gemini Integration
st.sidebar.markdown("---")
st.sidebar.subheader("🤖 Gemini AI Integration")
gemini_key_input = st.sidebar.text_input("Gemini API Key", type="password", help="Provide your personal Gemini API Key, or fallback to workspace secrets.")

# Set up active API Key using Session State or Secrets
if gemini_key_input:
    st.session_state["gemini_api_key"] = gemini_key_input
elif "GEMINI_API_KEY" in st.secrets:
    st.session_state["gemini_api_key"] = st.secrets["GEMINI_API_KEY"]
else:
    st.session_state["gemini_api_key"] = None

if st.session_state["gemini_api_key"]:
    st.sidebar.success("✅ Gemini API Key Loaded!")
else:
    st.sidebar.warning("⚠️ No Gemini API Key provided (Required for AI features).")

# Simple Authentication Mockup (Change details/credentials as needed for your class)
authorized = False
if username and password:
    if username == "student" and password == "erpnext2026":
        authorized = True
        st.sidebar.success("Authorized successfully!")
    else:
        st.sidebar.error("Invalid credentials.")

if authorized:
    st.subheader("🖥️ ERPNext Instance")
    # In a typical cloud setting, this iframe will target the public URL/port where ERPNext web service is exposed
    # Replace 'http://localhost:8000' with the deployed service or dynamic routing URL as needed
    target_url = st.text_input("ERPNext Server Address", value="http://localhost:8000")
    
    st.write(f"Connecting to ERPNext service at: `{target_url}`")
    components.iframe(target_url, height=700, scrolling=True)
else:
    st.info("Please log in via the sidebar to view the ERPNext workspace.")
