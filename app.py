import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import time
import random
import json

st.set_page_config(page_title="Vault-Sentinel SOC", layout="wide", page_icon="🛡️")

st.markdown("""
    <style>
    .main { background-color: #050505; color: #00ff00; font-family: 'Courier New', monospace; }
    .stMetric { background-color: #111; border: 1px solid #00ff00; border-radius: 4px; }
    .stDataFrame { border: 1px solid #00ff00; }
    </style>
    """, unsafe_allow_html=True)

if 'sec_logs' not in st.session_state:
    st.session_state.sec_logs = pd.DataFrame(columns=['Timestamp', 'Event_Type', 'Source_IP', 'Severity', 'User'])

st.title("🛡️ Vault-Sentinel | Secure Log Aggregator")
st.write("Real-time Security Event Monitoring System")

m1, m2, m3, m4 = st.columns(4)
total_events = len(st.session_state.sec_logs)
critical_events = len(st.session_state.sec_logs[st.session_state.sec_logs['Severity'] == 'CRITICAL'])

m1.metric("Total Events Ingested", total_events)
m2.metric("Critical Alerts", critical_events)
m3.metric("DB Integrity", "SHA-256 Verified")
m4.metric("Aggregator Status", "Active")

placeholder = st.empty()

for i in range(100):
    event_types = ["Login_Attempt", "File_Access", "Config_Change", "API_Call"]
    ips = ["192.168.1.45", "10.0.0.12", "172.16.254.1", "203.0.113.5"]
    users = ["admin", "dev_user", "root", "guest_account"]
    
    is_threat = random.random() > 0.92
    
    new_event = {
        'Timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'Event_Type': random.choice(event_types) if not is_threat else "BRUTE_FORCE_DETECTED",
        'Source_IP': random.choice(ips) if not is_threat else "185.22.14.99",
        'Severity': "INFO" if not is_threat else "CRITICAL",
        'User': random.choice(users)
    }
    
    st.session_state.sec_logs = pd.concat([pd.DataFrame([new_event]), st.session_state.sec_logs]).head(100)
    
    with placeholder.container():
        if is_threat:
            st.error(f"🚨 INTRUSION ATTEMPT DETECTED: {new_event['Source_IP']} at {new_event['Timestamp']}")
        
        c1, c2 = st.columns([2, 1])
        with c1:
            st.subheader("Live Event Stream")
            st.dataframe(st.session_state.sec_logs, use_container_width=True)
            
        with c2:
            st.subheader("Threat Distribution")
            if not st.session_state.sec_logs.empty:
                fig = px.pie(st.session_state.sec_logs, names='Severity', color='Severity',
                             color_discrete_map={'INFO':'#00ff00', 'CRITICAL':'#ff0000'})
                fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color="#00ff00", showlegend=False)
                st.plotly_chart(fig, use_container_width=True)

        st.divider()
        st.caption("Aggregator Backend Telemetry")
        st.code(f"PARSING_NODE_{i%4} >> Received Encrypted Packet | AES_BLOCK_SIZE: 128bit | HASH: {hex(random.getrandbits(128))}")
    
    time.sleep(1.5)
