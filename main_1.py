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


def read_data():
    conn = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM main_costumer;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    read_data()
