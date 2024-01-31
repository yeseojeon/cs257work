import psycopg2
from psycopg2 import sql

# This function sends an SQL query to the database
def test_query_one():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="jeony",
        user="jeony",
        password="eye362eye")

    cur = conn.cursor()

    firstsql = "SELECT lat, lon FROM us_cities WHERE city = 'Northfield' "
    
    cur.execute( firstsql )

    # fetchone() returns one row that matches your quer
    row = cur.fetchone()

    if row:
        print("Northfield's latitude is {row[0]}, longitude {row[1]}")
    else:
        print("Northfield is not in the database.")

    cur.close()
    conn.close()

test_query_one()



def test_query_two():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="jeony",
        user="jeony",
        password="eye362eye")

    cur = conn.cursor()

    secondsql = "SELECT * FROM us_cities ORDER BY population DESC;"
    
    cur.execute( secondsql )
    row = cur.fetchone()

    if row:
        print(row[0] + "has the most population.")

    cur.close()
    conn.close()

test_query_two()
