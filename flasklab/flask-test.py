import flask
import psycopg2
from psycopg2 import sql

app = flask.Flask(__name__)

#
@app.route('/hello')
def my_function():
    return "Hello World!"

@app.route('/display/<word1>/<word2>')
def my_display(word1, word2):
    the_string = "The words are: " + word1 + " and " + word2;
    return the_string

@app.route('/color/<word1>')
def my_color(word1):
    return '<h1 style="color:Green">' + word1 + '</h1>'

@app.route('/add/<num1>/<num2>')
def my_add(num1, num2):
    addition = int(num1) + int(num2)
    return str(addition)

@app.route('/pop/abbrev')
def my_pop(abbrev):
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="jeony",
        user="jeony",
        password="eye362eye")

    cur = conn.cursor()

    populationsql = "SELECT * FROM statepop WHERE code = %s' "

    cur.execute(populationsql, (abbrev,))

    population = cur.fetchone()[2]

    return str(population)

    cur.close()
    conn.close()


if __name__ == '__main__':
    my_port = 5126
    app.run(host='0.0.0.0', port = my_port) 
