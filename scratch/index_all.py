import requests
from oauth2client.service_account import ServiceAccountCredentials
import json
import time

# --- CONFIGURATION ---
# 1. Download Service Account JSON from Google Cloud Console
# 2. Add 'indexing-api@...' as 'Owner' in Search Console
# 3. Path to your JSON key
KEY_FILE = 'service_account.json'
SCOPES = ['https://www.googleapis.com/auth/indexing']

# --- URL LIST (Sitemap Harmony) ---
URLS = [
    "https://krisalaventis.in/",
    "https://krisalaventis.in/krisala-aventis-tathawade-flats-near-hinjewadi",
    "https://krisalaventis.in/krisala-aventis-tathawade-2-bhk-flats",
    "https://krisalaventis.in/krisala-aventis-tathawade-3-bhk-luxury-apartments",
    "https://krisalaventis.in/krisala-aventis-tathawade-construction-status",
    "https://krisalaventis.in/tathawade-connectivity-it-hubs.html",
    "https://krisalaventis.in/educational-hubs-near-krisala-aventis.html"
]

def authenticate():
    try:
        credentials = ServiceAccountCredentials.from_json_keyfile_name(KEY_FILE, SCOPES)
        return credentials
    except Exception as e:
        print(f"[-] Authentication Error: {e}")
        return None

def index_url(credentials, url):
    endpoint = "https://indexing.googleapis.com/v3/urlNotifications:publish"
    content = {
        "url": url,
        "type": "URL_UPDATED"
    }
    
    # Refresh token
    http = credentials.authorize(requests.Session())
    
    try:
        response = http.post(endpoint, json=content)
        if response.status_code == 200:
            print(f"[+] SUCCESS: {url} indexed.")
        else:
            print(f"[-] FAILED: {url} - {response.text}")
    except Exception as e:
        print(f"[-] Error indexing {url}: {e}")

if __name__ == "__main__":
    print("[*] Initiating Sovereign Indexing Sequence...")
    creds = authenticate()
    if creds:
        for url in URLS:
            index_url(creds, url)
            time.sleep(1) # Rate limit safety
    else:
        print("[!] Task Aborted: service_account.json not found.")
        print("[!] Please check implementation_plan.md for setup instructions.")
