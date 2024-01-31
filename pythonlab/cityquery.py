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
        print("Northfield's latitude is" + row[0] + ", longitude is" + row[1])
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
        print(row[0] + " has the most population.")

    cur.close()
    conn.close()

test_query_two()


def test_query_three():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="jeony",
        user="jeony",
        password="eye362eye")

    cur = conn.cursor()

    thirdsql = "SELECT city, state FROM us_cities WHERE state = 'Minnesota' ORDER BY population ASC;"
    
    cur.execute( thirdsql )
    row = cur.fetchone()

    if row:
        print(row[0] + " has the least population in MN.")

    cur.close()
    conn.close()

test_query_three()


#WRONG !!
def test_query_four():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="jeony",
        user="jeony",
        password="eye362eye")

    cur = conn.cursor()

    fourthsql = "SELECT city, lat, lon FROM us_cities ORDER BY lat DESC, lon ASC"
    
    cur.execute( fourthsql )
    rows = cur.fetchall()

    if rows:
        print("The names of the cities furthest North,"
              " furthest East, furthest South, and furthest"
              " West are respectively: " 
              + rows[0][0] + " " + rows[-1][0] + " " + rows[-2][0] 
              + " " + rows[1][0])

    cur.close()
    conn.close()

test_query_four()



'''
def test_query_five():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="jeony",
        user="jeony",
        password="eye362eye")

    cur = conn.cursor()

    fifthsql = "SELECT city, state FROM us_cities WHERE state = 'Minnesota' ORDER BY population ASC;"
    
    cur.execute( fifthsql )
    row = cur.fetchone()

    if row:
        print(row[0] + " has the least population in MN.")

    cur.close()
    conn.close()

test_query_five()
'''