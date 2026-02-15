# Secure Log Aggregator 🛡️

A centralized software hub that collects, encrypts, and audits system access logs to detect unauthorized network intrusions in real-time.

## Description
A centralized software hub that collects, encrypts, and audits system access logs to detect unauthorized network intrusions in real-time.

## Key Features
- **Anomaly Detection:** Identifies abnormal login frequencies and geographic IP mismatches.
- **Log Encryption:** Uses AES-256 to protect sensitive log data during storage.
- **Visual Audit Trail:** Interactive dashboard for searching and filtering security events.

## Tech Stack
- **Language:** Python
- **Libraries:** Streamlit, Pandas, Cryptography, Plotly
- **Model:** Frequency-based threshold analysis for intrusion detection.

## Engineering Logic
- **Backend:** The aggregator uses a multi-threaded watcher to monitor log file changes and applies a SHA-256 hash to ensure data integrity.
- **Software Engine:** A Streamlit interface visualizes "Threat Vectors," allowing administrators to block suspicious IPs instantly.
