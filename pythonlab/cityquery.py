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


def test_query_four():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="jeony",
        user="jeony",
        password="eye362eye")

    cur = conn.cursor()

    north_sql = "SELECT city FROM us_cities ORDER BY lat DESC LIMIT 1;"
    cur.execute(north_sql)
    furthest_north = cur.fetchone()

    east_sql = "SELECT city FROM us_cities ORDER BY lon DESC LIMIT 1;"
    cur.execute(east_sql)
    furthest_east = cur.fetchone()

    south_sql = "SELECT city FROM us_cities ORDER BY lat ASC LIMIT 1;"
    cur.execute(south_sql)
    furthest_south = cur.fetchone()

    west_sql = "SELECT city FROM us_cities ORDER BY lon ASC LIMIT 1;"
    cur.execute(west_sql)
    furthest_west = cur.fetchone()

    cur.close()
    conn.close()

    print("Furthest North city: " + furthest_north[0])
    print("Furthest East city: " + furthest_east[0])
    print("Furthest South city: " + furthest_south[0])
    print("Furthest West city: " + furthest_west[0])

test_query_four()



def test_query_five():
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="jeony",
        user="jeony",
        password="eye362eye")

    cur = conn.cursor()

    input_state = input("Enter a full state name or a state abbreviation: ")

    fifthsql = """
    SELECT state
    FROM states
    WHERE abbreviation = %s
    """

    cur.execute(fifthsql, (input_state,))
    
    state_name = cur.fetchone() or (input_state,)

    populationsql = """
    SELECT SUM(population)
    FROM us_cities 
    WHERE state = %s
    """

    cur.execute(populationsql, state_name)

    total_population = cur.fetchone()[0]

    print("The total population of " + input_state + " is " + str(total_population))

    cur.close()
    conn.close()

test_query_five()
