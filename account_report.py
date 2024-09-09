import requests
import json
from bs4 import BeautifulSoup
from itertools import cycle

# Function to report a TikTok account using a proxy
def report_with_proxy(username, proxy):
    report_url = "https://www.tiktok.com/feedback/report"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "username": username,
        "reason": "inappropriate content",
        "details": "This account is posting harmful content."
    }
    
    # Use proxy for the request
    proxies = {
        "http": proxy,
        "https": proxy
    }

    try:
        response = requests.post(report_url, headers=headers, data=data, proxies=proxies)
        if response.status_code == 200:
            print(f"Successfully reported {username} using proxy {proxy}")
        else:
            print(f"Failed to report {username} using proxy {proxy}. Status Code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to load configuration and start reporting
def main(config_file, username):
    # Load config
    with open(config_file, 'r') as file:
        config = json.load(file)

    # Extract proxy list from config
    proxy_list = config.get("proxies", [])
    if not proxy_list:
        print("No proxies found in configuration.")
        return
    
    # Rotate proxies
    proxy_pool = cycle(proxy_list)
    
    # Use the next proxy in the pool
    proxy = next(proxy_pool)
    
    # Report the account using the proxy
    report_with_proxy(username, proxy)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python3 account_report.py config.json username")
    else:
        config_file = sys.argv[1]
        username = sys.argv[2]
        main(config_file, username)