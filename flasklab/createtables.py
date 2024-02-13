#!/usr/bin/python

import psycopg2

def create_tables():

    command1 = """
        CREATE TABLE users ( 
            username text,
            password text
        )
        """
    conn = None

    try:
        # Connect to server and create a cursor
        conn = psycopg2.connect(
            host = "localhost",
            port = 5432,
            database = "kozakw",
            user = "kozakw",
            password = "summer862winter",
        )
        cur = conn.cursor()

        # Create each table
        cur.execute(command1)

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
