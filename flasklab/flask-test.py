#!/usr/bin/python

import flask
import psycopg2

app = flask.Flask(__name__)

conn = psycopg2.connect(
    host = "localhost",
    port = "5432",
    database = "kozakw",
    user = "kozakw",
    password = "summer862winter"
)
cur = conn.cursor()

@app.route('/hello')
def my_function():
    return "Hello World!"

@app.route('/display/<word1>/<word2>')
def my_display(word1, word2):
    the_string = "The words are: " + word1 + " and " + word2;
    return the_string

@app.route('/color/<word1>')
def my_color(word1):
    return '<h1 style="color:Red">' + word1 + '</h1>'

@app.route('/add/<num1>/<num2>')
def add(num1, num2):
    sum = int(num1) + int(num2)
    return str(sum)

@app.route('/pop/<abbrev>')
def get_population(abbrev):
    cur.execute("SELECT state_pop FROM state_pops WHERE state_id='" + abbrev.upper() + "';")
    pop = str(cur.fetchone()[0])
    if pop is None:
        return "Invalid state"
    return abbrev.upper() + ": " + pop

if __name__ == '__main__':
    my_port = 5127
    #my_other_port = 5227
    app.run(host='0.0.0.0', port = my_port) 

