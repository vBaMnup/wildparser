from dotenv import load_dotenv
from os import environ

load_dotenv()

HEADERS = {
    "Accept": "*/*",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Origin": environ.get("Origin"),
    "Pragma": "no-cache",
    "Referer": environ.get("Referer"),
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": environ.get("User-Agent"),
    "sec-ch-ua": environ.get("sec-ch-ua"),
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": environ.get("sec-ch-ua-platform"),
}

DELAY = int(environ.get("DELAY"))
TELEGRAM_TOKEN = environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = environ.get("TELEGRAM_CHAT_ID")
