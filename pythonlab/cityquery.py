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
    cur.execute("SELECT city_name FROM cities WHERE city_name='Northfield';")
    result = cur.fetchone()
    
    if result == None:
        print("Northfield is not found in the database.")
        return

    cur.execute("SELECT city_lat,city_lon FROM cities WHERE city_name='Northfield';")
    location = cur.fetchone()
    print("lat: " + str(location[0]) + ", lon: " + str(location[1]))

def query_two():
    cur.execute("SELECT city_name FROM cities ORDER BY city_pop DESC;")
    largest_city = cur.fetchone()
    print("Largest City: " + str(largest_city[0]))

def query_three():
    cur.execute("SELECT city_name FROM cities WHERE state_name='Minnesota' ORDER BY city_pop;")
    smallest_mn_city = cur.fetchone()
    print("Smallest City in Minnesota: " + str(smallest_mn_city[0]))

def query_four():
    cur.execute("SELECT city_name FROM cities ORDER BY city_lat DESC;")
    north = cur.fetchone()
    print("Farthest North: " + north[0])

    cur.execute("SELECT city_name FROM cities ORDER BY city_lon DESC;")
    east = cur.fetchone()
    print("Farthest East: " + east[0])

    cur.execute("SELECT city_name FROM cities ORDER BY city_lat;")
    south = cur.fetchone()
    print("Farthest South: " + south[0])

    cur.execute("SELECT city_name FROM cities ORDER BY city_lon;")
    west = cur.fetchone()
    print("Farthest West: " + west[0])

query_one()
query_two()
query_three()
query_four()
