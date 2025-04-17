from connect import connect
 
def delete_data():
    delete_option = input("Enter the option to delete by (name/phone): ").lower()
    value = input(f"Enter the {delete_option} to delete: ")
 
    conn = connect()
    cur = conn.cursor()
 
    if delete_option == 'name':
        cur.execute("DELETE FROM phonebook WHERE name = %s", (value,))
    elif delete_option == 'phone':
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (value,))
    else:
        print("Invalid delete option.")
        return
 
    conn.commit()
    cur.close()
    conn.close()
    print(f"User with {delete_option} {value} deleted from the PhoneBook.")
 
if __name__ == '__main__':
    delete_data()