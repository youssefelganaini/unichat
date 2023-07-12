import psycopg2

conn = psycopg2.connect(
    host="localhost", dbname="Newsletter", user="postgres", password="1234"
)

cur = conn.cursor()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS
    """
)
