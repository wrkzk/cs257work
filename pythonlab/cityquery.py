#!usr/bin/python

import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    port = 5432,
    database = "kozakw",
    user = "kozakw",
    password = "summer862winter",
)
cur = conn.cursor()

def query_one():
    cur.execute("SELECT city_name FROM cities WHERE city_name='Northfield'")
    result = cur.fetchone()
    
    if result == None:
        print("Northfield is not found in the database.")
        return

    print(result)

query_one()
