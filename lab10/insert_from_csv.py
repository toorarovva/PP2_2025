import csv
from connect import connect
 
def insert_from_csv(csv_file):
    conn = connect()
    cur = conn.cursor()
 
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['name']
            phone = row['phone']
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
 
    conn.commit()
    cur.close()
    conn.close()
    print(f"Data from {csv_file} inserted into the PhoneBook.")
 
if __name__ == '__main__':
    insert_from_csv('lab10/contacts.csv')