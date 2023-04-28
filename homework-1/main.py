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
                for i in reader:
                    cur.execute("INSERT INTO customers_name VALUES (%s, %s, %s)",
                                (i["customer_id"], i["company_name"], i["contact_name"]))
        conn.close()


def import_in_employees_data(url_file='./north_data/employees_data.csv'):
    """
    Импортирует из employees_data.csv в БД одноименную таблицу
    """
    with open(url_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        with psycopg2.connect(host="localhost", database="north", user="postgres", password=password_bd) as conn:
            with conn.cursor() as cur:
                print(cur)
                for i in reader:
                    cur.execute("INSERT INTO employees_data VALUES (%s, %s, %s, %s, %s)",
                                (i["first_name"], i["last_name"], i["title"], i["birth_date"], i["notes"]))
        conn.close()


def import_in_orders_data(url_file='./north_data/orders_data.csv'):
    """
    Импортирует из orders_data.csv в БД одноименную таблицу
    """
    with open(url_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        with psycopg2.connect(host="localhost", database="north", user="postgres", password=password_bd) as conn:
            with conn.cursor() as cur:
                for i in reader:
                    cur.execute("INSERT INTO orders_data VALUES (%s, %s, %s, %s, %s)",
                                (i["order_id"], i["customer_id"], i["employee_id"], i["order_date"], i["ship_city"]))
        conn.close()


#import_in_customers_data()
#import_in_orders_data()
#import_in_employees_data()