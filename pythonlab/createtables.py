import psycopg2
from psycopg2 import sql

def test_connection():
    try:
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            database="jeony",
            user="jeony",
            password="eye362eye"
        )

        if conn is not None:
            print("Connected!")
        else:
            print("Not Connected.")

        # SQL statements to drop and create the "states" table
        drop_states_sql = """ DROP TABLE IF EXISTS states; """
        create_states_sql = """
            CREATE TABLE states ( state text, abbreviation text);
        """

        # SQL statements to drop and create the "us_cities" table
        drop_cities_sql = """ DROP TABLE IF EXISTS us_cities; """
        create_cities_sql = """
            CREATE TABLE us_cities ( city text, state text, population int, 
            lat real, lon real
            );
        """

        cur = conn.cursor()
        cur.execute(sql.SQL(drop_states_sql))
        cur.execute(sql.SQL(create_states_sql))

        cur.execute(sql.SQL(drop_cities_sql))
        cur.execute(sql.SQL(create_cities_sql))

        conn.commit()


test_connection()
