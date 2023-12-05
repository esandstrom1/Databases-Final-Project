# app.py
from flask import Flask, render_template, request, jsonify
import sqlite3
from user_query import print_state
import subprocess

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/on_click', methods=['POST'])
def on_click():
    data = request.get_json()
    x = data['x']
    y = data['y']
    result = call_state(x, y)
    return {'result': result}


def call_state(x, y):
    try:
        result = print_state("Alaska", 2001)

        result_and_coordinates = f"Clicked at ({x}, {y})\n" + result
        return result_and_coordinates

    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

    return f"Clicked at ({x}, {y})"



if __name__ == '__main__':
    app.run(debug=True, port=8000)
