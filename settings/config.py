from dotenv import load_dotenv
from os import environ
import logging
from random import randint

load_dotenv()

logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO)

HEADERS = {
    "Accept": "*/*",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Origin": environ.get("ORIGIN"),
    "Pragma": "no-cache",
    "Referer": environ.get("REFERER"),
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": environ.get("USERAGENT"),
    "sec-ch-ua": environ.get("SECCHUA"),
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": environ.get("SECCHUAPLATFORM"),
}

DELAY = randint(600, 3600)
TELEGRAM_TOKEN = environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = environ.get("TELEGRAM_CHAT_ID")
