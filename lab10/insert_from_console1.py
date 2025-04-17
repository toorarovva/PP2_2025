from connect1 import connect
 
def insert_from_console():

    name = input("Enter the user's name: ")

    conn = connect()

    if conn is None:

        print("❌ Failed to connect to the database.")

        return
 
    cur = conn.cursor()

    cur.execute("SELECT id FROM \"user\" WHERE username = %s", (name,))

    user = cur.fetchone()

    if user:

        user_id = user[0]

        print(f"Welcome back, {name}!")

    else:

        cur.execute("INSERT INTO \"user\" (username) VALUES (%s) RETURNING id", (name,))

        user_id = cur.fetchone()[0]

        print(f"User {name} created.")
 
    conn.commit()

    cur.close()

    conn.close()
 
    return user_id
 
if __name__ == '__main__':

    insert_from_console()

 