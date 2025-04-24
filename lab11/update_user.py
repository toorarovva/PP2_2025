import psycopg2

conn = psycopg2.connect(dbname="phonebook_db", user="postgres", password="1234", host="localhost")
cur = conn.cursor()


user_id = int(input("id to update:"))
new_name = input("new name: ")
new_phone = input("new phone: ")

cur.execute("""
    UPDATE users
    SET name = %s, phone = %s
    WHERE id = %s
""", (new_name, new_phone, user_id))

conn.commit()
cur.close()
conn.close()

print("successfully")
