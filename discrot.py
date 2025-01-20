import time
import requests
from dotenv import load_dotenv
import os

# Kode warna ANSI
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

# Function to send a message to the channel
def send_message(content):
    url = f"https://discord.com/api/v10/channels/{CHANNEL_ID}/messages"
    data = {"content": content}
    response = requests.post(url, headers=HEADERS, json=data)
    
    if response.ok:
        print(f"{GREEN}Sent: {content}{RESET}")
    else:
        print(f"{RED}Failed to send message: {response.status_code} - {response.text}{RESET}")

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

if not TOKEN or not CHANNEL_ID:
    print(f"{RED}Error: Missing environment variables. Check your .env file.{RESET}")
    exit(1)

HEADERS = {
    "Authorization": f"{TOKEN}",
    "Content-Type": "application/json"
}

# Function to test the token
def test_personal_token():
    url = "https://discord.com/api/v10/users/@me"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        print(f"{GREEN}Token is valid! Logged in as: {response.json()['username']}{RESET}")
    else:
        print(f"{RED}Token test failed: {response.status_code} - {response.text}{RESET}")
        exit(1)

# Test the personal token
test_personal_token()

# Main loop to send a message every 12 hours
def main():
    message_content = "<@1322128247550640130> 0xd93683ac23dac8e1ef3eae1ac4cca5658c44dd29d16a19256343f88cdbbfcd9d"
    while True:
        try:
            send_message(message_content)
            time.sleep(12 * 60 * 60)  # 24 hours in seconds
        except Exception as e:
            print(f"{RED}Error occurred: {e}{RESET}")
            time.sleep(300)  # Retry after 5 minutes

# Run the script
if __name__ == "__main__":
    main()
