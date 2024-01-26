#!/usr/bin/python

import psycopg2

def create_tables():

    command1 = """
        CREATE TABLE states ( 
            state_name text NOT NULL,
            state_id text
        )
        """
    command2 = """
        CREATE TABLE cities (
            city_name text NOT NULL,
            state_name text NOT NULL,
            city_pop int NOT NULL,
            city_lat real NOT NULL,
            city_lon real NOT NULL
        )
        """
    conn = None

    try:
        # Connect to server and create a cursor
        conn = psycopg2.connect(
            host = "localhost",
            port = 5432,
            database = "kozakw"
            user = "kozakw"
            password = ""
        )
        cur = conn.cursor()

        # Create each table
        cur.execute(command1)
        cur.execute(command2)

        # Close connect to server and commit changes
        cur.close()
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    create_tables()
