import psycopg2
from psycopg2 import sql

def test_connection():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="jeony",
        user="jeony",
        password="eye362eye")

    if conn is not None:
        print("Connection Worked!")
    else:
        print("Problem with Connection")

    drop_statepop_sql = """ DROP TABLE IF EXISTS statepop; """
    create_statepop_sql = """
        CREATE TABLE statepop (
            code text,
            state text,
            pop real
        );
    """

    cur = conn.cursor()
    cur.execute(sql.SQL(drop_statepop_sql))
    cur.execute(sql.SQL(create_statepop_sql))

    conn.commit()
    conn.close()

test_connection()
