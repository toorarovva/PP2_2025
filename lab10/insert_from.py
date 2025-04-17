from connect import connect
 
def insert_from_console():
    name = input("Enter the user's name: ")
    phone = input("Enter the user's phone: ")
 
    conn = connect()
    if conn is None:
        print("❌ Failed to connect to the database.")
        return
 
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit()
        print(f"User {name} with phone {phone} inserted into the PhoneBook.")
    except Exception as e:
        print(f"❌ Error while inserting data: {e}")
    finally:
        cur.close()
        conn.close()
 
if __name__ == '__main__':
    insert_from_console()