import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

print("TOKEN:", BOT_TOKEN)

url = f"https://api.telegram.org/bot{BOT_TOKEN}/getMe"

response = requests.get(url)

print(response.status_code)
print(response.text)
