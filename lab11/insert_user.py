import psycopg2

conn = psycopg2.connect(dbname="phonebook_db", user="postgres", password="1234", host="localhost")

cur = conn.cursor()

name = input("name: ")
surname = input("surname: ")
phone = input("phone: ")

cur.execute("INSERT INTO users (name, surname, phone) VALUES (%s, %s, %s)", (name, surname, phone))

conn.commit()
cur.close()
conn.close()

print("inserted successfully")
