import requests
import hashlib
import time
import os

# Configuration
SERVER_URL = "http://localhost:8000/verify" # Change to Backend IP in production
AGENT_ID = "linux-server-01"
FILES_TO_WATCH = ["./important.txt"] # Add paths to critical files here

def get_sha256(filename):
    sha256_hash = hashlib.sha256()
    with open(filename, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def run_monitor():
    print(f"[*] Starting Sentinel Agent: {AGENT_ID}")
    while True:
        for file_path in FILES_TO_WATCH:
            if os.path.exists(file_path):
                file_hash = get_sha256(file_path)
                data = {
                    "agent_id": AGENT_ID,
                    "file_path": file_path,
                    "current_hash": file_hash
                }
                try:
                    response = requests.post(SERVER_URL, json=data)
                    print(f"[+] Checked {file_path}: {response.json()}")
                except Exception as e:
                    print(f"[!] Server unreachable: {e}")
            else:
                print(f"[!] File missing: {file_path}")
        
        time.sleep(10) # Check every 10 seconds

if __name__ == "__main__":
    run_monitor()