import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Sentinel-FIM Dashboard", layout="wide")
st.title("🛡️ Sentinel-FIM Security Console")

# Sidebar for status
st.sidebar.header("System Status")
st.sidebar.success("Manager: Online")

# Fetch Alerts from Backend
try:
    response = requests.get("http://backend:8000/alerts") # Use 'backend' because of Docker network
    alert_data = response.json()
    
    if alert_data:
        st.error(f"CRITICAL: {len(alert_data)} Integrity Violations Found!")
        df = pd.DataFrame(alert_data)
        st.table(df)
    else:
        st.balloons()
        st.success("No tampering detected. All systems integral.")
        
except:
    st.warning("Waiting for connection to Backend Manager...")

if st.button('Refresh Data'):
    st.rerun()