import psycopg2
import http

conn = psycopg2.connect(
    host="localhost", dbname="youssef", user="postgres", password="1234"
)

cur = conn.cursor()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY,
    name TEXT,
    email TEXT,
    keywords TEXT,
    language TEXT,
    country TEXT
    );
    """
)


def getCurrentID():
    query = "SELECT COUNT(*) from users;"
    cur.execute(query)
    return cur.fetchone()[0]


def addUserToDB(name, email, keywords, language, country):
    cur = conn.cursor()
    try:
        currentID = getCurrentID() + 1
        query = "INSERT INTO users (id, name, email, keywords, language, country) VALUES(%s, %s, %s, %s, %s, %s)"
        cur.execute(query, (currentID, name, email, keywords, language, country))
    except (Exception, psycopg2.Error) as error:
        print("Error in adding user operation - ", error)
        return http.HTTPStatus.BAD_REQUEST
    conn.commit()
    cur.close()
    return http.HTTPStatus.ACCEPTED


def deleteUserFromDB(email):
    try:
        query = "DELETE from users WHERE email = %s"
        cur.execute(query, (email,))
    except (Exception, psycopg2.Error) as error:
        print("Error in deleting user operation - ", error)
        return http.HTTPStatus.BAD_REQUEST
    conn.commit()
    return http.HTTPStatus.ACCEPTED


conn.commit()
# cur.close()
# conn.close()
