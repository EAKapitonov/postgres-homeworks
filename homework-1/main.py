"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2
import os

password_bd: str = os.getenv('password_bd')


def import_in_customers_data(url_file='./north_data/customers_data.csv'):
    """
    Импортирует из customers_data.csv в БД одноименную таблицу
    """
    with open(url_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        with psycopg2.connect(host="localhost", database="north", user="postgres", password=password_bd) as conn:
            with conn.cursor() as cur:
                print(cur)
                for i in reader:
                    print(cur)
                    print(i["customer_id"], i["company_name"], i["contact_name"])
                    cur.execute("INSERT INTO customers_data VALUES (%s, %s, %s)",
                                (i["customer_id"], i["company_name"], i["contact_name"]));
        conn.close()


def import_in_employees_data():
    """
    Импортирует из employees_data.csv в БД одноименную таблицу
    """
    pass


def import_in_orders_data():
    """
    Импортирует из orders_data.csv в БД одноименную таблицу
    """
    pass


import_in_customers_data()
