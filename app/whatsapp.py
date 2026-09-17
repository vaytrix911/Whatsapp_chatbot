import requests
from app.config import ACCESS_TOKEN, PHONE_NUMBER_ID

def parse_incoming(data):
    message = data["entry"][0]["changes"][0]["value"]["messages"][0]
    sender = message["from"]
    text = message["text"]["body"]
    return sender,text

def send_reply(to, text):
    url = f"https://graph.facebook.com/v23.0/{PHONE_NUMBER_ID}/messages"

    headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json",}

    data = {
    "messaging_product": "whatsapp",
    "to": to,
    "type": "text",
    "text": {
        "body": text
    }}

    response = requests.post(
    url,
    headers=headers,
    json=data)
    response.raise_for_status()