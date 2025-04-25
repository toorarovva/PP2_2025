import psycopg2

conn = psycopg2.connect(dbname="phonebook_db", user="postgres", password="1234", host="localhost")
cur = conn.cursor()

name_or_phone = input("name or phone to delete: ")


cur.execute("""
    DELETE FROM users
    WHERE name = %s OR phone = %s
""", (name_or_phone, name_or_phone))

conn.commit()


cur.close()
conn.close()


print("deleted")
