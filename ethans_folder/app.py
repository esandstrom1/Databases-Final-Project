# app.py
from flask import Flask, render_template, request, jsonify
import sqlite3
from user_query import print_state
import subprocess

global_state = "Ohio"

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/on_update', methods=['POST'])
def on_update():
    data = request.get_json()
    x = data['x']
    y = data['y']
    year = data['year']
    result = call_state(x, y, year)
    return {'result': result}


def call_state(x, y, year):
    global global_state
    if x >= 165 and x <= 218:
        if y >= 165 and y <= 218:
            state = "Alaska"
            global_state = "Alaska"
    if x == 0 and y == 0:
        state = global_state


    try:
        result = print_state(state, year)
        result_and_coordinates = f"Clicked at ({x}, {y})\n" + result
        return result_and_coordinates
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"




if __name__ == '__main__':
    app.run(debug=True, port=8000)
