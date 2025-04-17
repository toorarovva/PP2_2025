from connect import connect
 
def query_data():
    filter_option = input("Enter filter option (name/phone): ").lower()
    value = input(f"Enter the {filter_option} to search: ")
 
    conn = connect()
    cur = conn.cursor()
 
    if filter_option == 'name':
        cur.execute("SELECT * FROM phonebook WHERE name = %s", (value,))
    elif filter_option == 'phone':
        cur.execute("SELECT * FROM phonebook WHERE phone = %s", (value,))
    else:
        print("Invalid filter option.")
        return
 
    results = cur.fetchall()
    for row in results:
        print(row)
 
    conn.close()
 
if __name__ == '__main__':
    query_data()