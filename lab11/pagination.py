import psycopg2

def get_users_page(limit, offset):
    conn = psycopg2.connect(dbname="phonebook_db", user="postgres", password="1234", host="localhost")
    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM users
        ORDER BY id
        LIMIT %s OFFSET %s
    """, (limit, offset))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
