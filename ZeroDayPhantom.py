import requests
from bs4 import BeautifulSoup
from itertools import cycle
import time
import sys

# Function to display the ZeroDayPhantom banner
def display_banner():
    banner = """
    ███████╗███████╗██████╗  ██████╗ ██████╗  █████╗ ██╗   ██╗███████╗████████╗
    ██╔════╝██╔════╝██╔══██╗██╔════╝ ██╔══██╗██╔══██╗██║   ██║██╔════╝╚══██╔══╝
    ███████╗█████╗  ██████╔╝██║  ███╗██████╔╝███████║██║   ██║███████╗   ██║   
    ╚════██║██╔══╝  ██╔═══╝ ██║   ██║██╔═══╝ ██╔══██║██║   ██║╚════██║   ██║   
    ███████║███████╗██║     ╚██████╔╝██║     ██║  ██║╚██████╔╝███████║   ██║   
    ╚══════╝╚══════╝╚═╝      ╚═════╝ ╚═╝     ╚═╝  ╚═════╝ ╚══════╝   ╚═╝   
    """
    print(banner)

# Function to get TikTok user information and check if it exists
def get_tiktok_user_info(username):
    url = f"https://www.tiktok.com/@{username}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(f"\n[+] Username '{username}' found!")
        return True
    else:
        print(f"\n[-] Username '{username}' not found.")
        return False

# Function to report a TikTok account
def report_tiktok_account(username):
    report_url = "https://www.tiktok.com/feedback/report"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "username": username,
        "reason": "inappropriate content",  # Example reason
        "details": "This account is posting harmful content."
    }
    response = requests.post(report_url, headers=headers, data=data)
    if response.status_code == 200:
        print(f"\n[+] Successfully reported '{username}'")
    else:
        print(f"\n[-] Failed to report '{username}'")

# Function to report using proxies to bypass rate limiting
def report_with_proxy(username):
    proxies = [
        "http://proxy1.com",
        "http://proxy2.com",
        "http://proxy3.com"
    ]
    proxy_pool = cycle(proxies)
    proxy = next(proxy_pool)
    report_url = "https://www.tiktok.com/feedback/report"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    data = {
        "username": username,
        "reason": "inappropriate content"
    }
    response = requests.post(report_url, headers=headers, data=data, proxies={"http": proxy, "https": proxy})
    print(response.status_code, response.text)

# Main function
def main():
    display_banner()
    
    # Prompt user to insert username
    username = input("\nEnter TikTok username: ")

    # Check if username exists
    if get_tiktok_user_info(username):
        # Display options
        print("\nOptions:")
        print("1. Start report")
        print("2. Abort")
        choice = input("\nEnter your choice (1/2): ")

        if choice == '1':
            report_with_proxy(username)
        elif choice == '2':
            print("\n[-] Aborted.")
        else:
            print("\n[-] Invalid choice. Aborting.")
    else:
        print("\n[-] Aborting process.")

if __name__ == "__main__":
    main()
