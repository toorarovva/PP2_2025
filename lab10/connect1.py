import psycopg2

from config import load_config
 
def connect():

    config = load_config('lab10/database.ini')

    try:

        conn = psycopg2.connect(**config)

        print("✅ Connected to the PostgreSQL server.")

        return conn

    except Exception as error:

        print("❌ Connection error:", error)

        return None


 