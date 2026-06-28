import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(page_title="ERPNext Lab Control Portal", layout="wide")

st.title("🎓 ERPNext Lab Control Portal")
st.write("Welcome to the cloud-based ERPNext student lab. Authorize via the sidebar to access your ERPNext environment.")

# Sidebar API Configuration
st.sidebar.subheader("🤖 Gemini AI Integration")
gemini_key_input = st.sidebar.text_input("Gemini API Key", type="password", help="Provide your personal Gemini API Key to unlock the control portal.")

# Set up active API Key using Session State or Secrets
if gemini_key_input:
    st.session_state["gemini_api_key"] = gemini_key_input
elif "GEMINI_API_KEY" in st.secrets:
    st.session_state["gemini_api_key"] = st.secrets["GEMINI_API_KEY"]
else:
    st.session_state["gemini_api_key"] = None

# If API key is present, let them inside the portal
if st.session_state["gemini_api_key"]:
    st.sidebar.success("✅ Access Granted (API Key Loaded!)")
    
    st.subheader("🖥️ ERPNext Instance")
    target_url = st.text_input("ERPNext Server Address", value="http://localhost:8000")
    
    st.write(f"Connecting to ERPNext service at: `{target_url}`")
    components.iframe(target_url, height=700, scrolling=True)
    
    # Student credentials sidebar comes later
    st.sidebar.markdown("---")
    st.sidebar.subheader("🔑 Student Authentication")
    username = st.sidebar.text_input("Student Username")
    password = st.sidebar.text_input("Password", type="password")
    if username and password:
        if username == "student" and password == "erpnext2026":
            st.sidebar.success("Student authorized!")
        else:
            st.sidebar.error("Invalid credentials.")
else:
    st.info("🔑 Please enter your Gemini API Key in the sidebar to access the ERPNext Portal.")

