import psycopg2

conn = psycopg2.connect(
    host="localhost", dbname="Newsletter", user="postgres", password="1234"
)

cur = conn.cursor()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY
    name TEXT,
    email TEXT,
    keywords TEXT,
    language TEXT,
    country TEXT
    );
    """
)


def addUser(name, email, keywords, language, country):
    try:
        query = "INSERT INTO users (name, email, keywords, language country) VALUES(%s, %s, %s, %s, %s)"
        cur.execute(query, (name, email, keywords, language, country))
    except (Exception, psycopg2.Error) as error:
        print("Error in adding user operation", error)


def deleteUser(email):
    query = "DELETE from users WHERE email = %s"
    cur.execute(query, email)


def update_email(new_email):
    query = ""


conn.commit()
cur.close()
conn.close()
