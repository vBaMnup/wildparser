import logging

from settings.config import DELAY, HEADERS
from parcer.wild_parcer import proccesed


def main():
    logging.info("Start!")
    with open("parcer/links.txt", "r", encoding="utf-8") as file:
        links = file.read().splitlines()

    proccesed(links, HEADERS, DELAY)


if __name__ == "__main__":
    while True:
        main()
