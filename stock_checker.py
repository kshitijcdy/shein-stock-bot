import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

print("BOT_TOKEN =", BOT_TOKEN)
print("CHAT_ID =", CHAT_ID)

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

response = requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": "🚨 GitHub Test Message"
    }
)

print(response.text)
