import requests
from time import sleep
from .bot import send_message

from .database import insert_product, get_product_by_name, close_db


def parse(response_text):
    products = response_text.json()["data"]["products"]
    parsed_data = []
    for i in products:
        product_id = i.get("id")
        name = i.get("name") + str(product_id)
        price = i.get("salePriceU") // 100
        link = f"https://www.wildberries.ru/catalog/{product_id}/detail.aspx"
        parsed_data.append({"name": name, "price": price, "link": link})
    return parsed_data


def get_html(url, headers):
    response = requests.get(url=url, headers=headers)
    parsed_data = parse(response)

    for item in parsed_data:
        existing_product = get_product_by_name(item["name"])
        if existing_product:
            if existing_product[2] > item["price"]:
                message = (
                    f"Цена на товар {existing_product[1]} изменилась с {existing_product[2]} руб. на {item['price']} руб."
                    f"\n{existing_product[3]}"
                )
                send_message(message)
        else:
            insert_product(item["name"], item["price"], item["link"])

    return parsed_data


def proccesed(links, headers, delay):
    for link in links:
        get_html(link, headers)
        sleep(delay)
    close_db()


if __name__ == "__main__":
    proccesed()
