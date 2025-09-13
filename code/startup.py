#!/usr/bin/env python3
import subprocess
import sys
import requests
import os

def get_public_ip():
    """Get the current public IP address"""
    try:
        response = requests.get('https://ifconfig.me', timeout=5)
        return response.text.strip()
    except:
        try:
            response = requests.get('https://api.ipify.org', timeout=5)
            return response.text.strip()
        except:
            return "localhost"

def main():
    print("Fetching current public IP...")
    public_ip = get_public_ip()
    print(f"Current public IP: {public_ip}")
    
    # Generate certificates with current IP
    print(f"Generating SSL certificates for: localhost, 127.0.0.1, ::1, {public_ip}")
    
    # Run mkcert command
    cmd = [
        "mkcert", 
        "-key-file", "/app/certs/key.pem", 
        "-cert-file", "/app/certs/cert.pem", 
        "localhost", "127.0.0.1", "::1", public_ip
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error generating certificates: {result.stderr}")
        sys.exit(1)
    
    print("Certificates generated successfully!")
    return True

if __name__ == "__main__":
    main()
