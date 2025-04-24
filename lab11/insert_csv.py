import psycopg2
import csv

conn = psycopg2.connect(dbname="phonebook_db", user="postgres", password="1234", host="localhost")
cur = conn.cursor()


with open(r'C:\Users\User\OneDrive\Рабочий стол\PP2_2025\lab11\users.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  
    for row in reader:
        name, surname, phone = row
        cur.execute("INSERT INTO users (name, surname, phone) VALUES (%s, %s, %s)", (name, surname, phone))

conn.commit()
cur.close()
conn.close()

print("inserted successfully")
