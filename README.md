# Sentinel-FIM: Distributed File Integrity Monitor
Sentinel-FIM is a full-stack cybersecurity solution designed to monitor the integrity of critical system files across multiple remote endpoints. By leveraging a centralized manager and lightweight agents, it detects unauthorized file modifications, deletions, and creations in real-time using SHA-256 cryptographic hashing.

# 🚀 Features
Distributed Architecture: Centralized FastAPI manager handles logic while remote Python agents perform edge-side hashing.

Real-Time Detection: Identifies file tampering within 60 seconds of the event.

Persistent Audit Trail: All integrity violations are logged in a PostgreSQL database for forensic analysis.

Visual Dashboard: Streamlit-based UI provides a high-level overview of agent health and recent alerts.

Containerized Deployment: Orchestrated via Docker Compose for rapid, scalable deployment.

# 🛠️ Tech Stack
Language: Python 3.10+

Backend: FastAPI (Asynchronous API)

Frontend: Streamlit

Database: PostgreSQL

Security: SHA-256 Hashing, HMAC (optional), Network Isolation

DevOps: Docker, Docker Compose

# 📂 Project Structure
Plaintext
Sentinel-FIM/
├── backend/            # FastAPI Manager & DB Logic
├── frontend/           # Streamlit Dashboard
├── agent/              # Lightweight Monitoring Script
├── docker-compose.yml  # Orchestration file
└── README.md           # Documentation
🚦 Getting Started
Prerequisites
Docker and Docker Compose installed.

Python 3.x (for running the agent).

# Installation
Clone the repository:

Bash
git clone https://github.com/yourusername/Sentinel-FIM.git
cd Sentinel-FIM

# Spin up the infrastructure:
Bash
docker-compose up --build
Dashboard: http://localhost:8501

API Docs: http://localhost:8000/docs

# Run an Agent:
Navigate to the /agent folder on a target machine and run:

Bash
python agent.py
🛡️ Security Use Cases
Web Server Protection: Monitor /var/www/html for unauthorized code injection.

System Hardening: Track changes to /etc/passwd or /etc/shadow.

Compliance: Maintain an audit trail of file access and modifications for regulatory requirements.
