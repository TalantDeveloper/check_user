import os
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')
import psycopg2


def connect():
    try:
        conn = psycopg2.connect(
            dbname="asterisk",
            user="postgres",
            password="@Botirjon06",
            host="localhost",
            port=5432
        )
        print("Connected to the database")
        return conn
    except Exception as e:
        print(f"An error occurred: {e}")


def read_data(table_name):
    conn = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name};")
        rows = cursor.fetchall()
        return rows
        cursor.close()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if conn is not None:
            conn.close()

