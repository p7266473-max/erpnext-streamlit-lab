# 🚀 ERPNext Streamlit Lab Orchestration

This repository contains the orchestration and portal dashboard for deploying a cloud-based ERPNext laboratory using Docker containers and Streamlit.

## Files Included

- `docker-compose.yml`: Pulls the official Frappe/ERPNext images and starts databases and services.
- `app.py`: Streamlit control portal offering user authentication and iframe embedding of the running ERPNext service.
- `requirements.txt`: Streamlit environment packages.

---

## 🔒 Deployment Strategy (Streamlit Community Cloud)

1. **Step 1: Public Handshake (Public Repository)**
   - Create a **Public** repository on GitHub (completed automatically below).
   - Go to [Streamlit Community Cloud](https://streamlit.io/cloud), log in, and deploy this app pointing to the public repository (`app.py`).
   - Confirm that the Streamlit application performs its initial handshake, builds, and starts successfully.

2. **Step 2: Transitioning to Private**
   - Once the handshake is complete and the site is active, go to your GitHub repository settings.
   - Scroll down to the **Danger Zone** and select **Change repository visibility** -> **Make private**.
   - Because Streamlit authorized with GitHub OAuth permissions originally, it retains access to pull your private repository code securely while denying external public access to your configuration files.
