import sqlite3
import os.path

if not os.path.isfile("products.db"):
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE products 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price INTEGER, link TEXT)"""
    )
    conn.commit()
else:
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()


def insert_product(name, price, link):
    cursor.execute(
        "INSERT INTO products (name, price, link) VALUES (?,?,?)",
        (name, price, link),
    )
    conn.commit()


def update_product(id, price):
    cursor.execute(
        "UPDATE products SET price=? WHERE id=?",
        (price, id),
    )
    conn.commit()


def get_product_by_name(name):
    cursor.execute("SELECT * FROM products WHERE name=?", (name,))
    return cursor.fetchone()


def close_db():
    conn.close()
