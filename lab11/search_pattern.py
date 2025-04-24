import psycopg2

conn = psycopg2.connect(dbname="phonebook_db", user="postgres", password="1234", host="localhost")
cur = conn.cursor()


pattern = input("Enter pattern to search for: ")


cur.execute("SELECT * FROM users WHERE name ILIKE %s OR surname ILIKE %s OR phone ILIKE %s", ('%' + pattern + '%', '%' + pattern + '%', '%' + pattern + '%'))
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()
