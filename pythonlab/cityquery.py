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

    cur.execute("SELECT city_lat,city_lon FROM cities WHERE city_name='Northfield'")
    location = cur.fetchone()
    print("lat: " + str(location[0]) + ", lon: " + str(location[1]))

def query_two():
    cur.execute("SELECT TOP 1 city_name FROM cities ORDER BY city_pop")
    largest_city = cur.fetchone()
    print(largest_city)

query_one()
query_two()
