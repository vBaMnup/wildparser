import requests

from settings.config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID


def send_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    params = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    response = requests.post(url, params=params)
    return response
