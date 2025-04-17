import psycopg2
from connect import connect

def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            phone VARCHAR(20)
            );
    ''')
    conn.commit()
    cur.close()
    conn.close()
    print("📁 Table 'phonebook' created.")

if __name__ == '__main__':
    create_table()
