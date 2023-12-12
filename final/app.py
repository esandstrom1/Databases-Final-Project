# app.py
from flask import Flask, render_template, request, jsonify
import sqlite3
from user_query import print_state, state_total
import subprocess

# local
from find_cords import build_state_with_cords

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
    # result = print_cords(x, y)
    return {'result': result}


def print_cords(x, y):
    return f"x: {x}, y: {y}"

#

def call_state(x, y, year):
    global global_state
    states_with_cords = build_state_with_cords()
    for st, cord_tup in states_with_cords.items():
        p1, p2 = cord_tup
        if x >= p1[0] and x <= p2[0]:
            if y >= p1[1] and y <= p2[1]:
                print(st)
                state = st
                global_state = st
        else:
            state = global_state

    try:
        #Get the coordinates for the graph
        totals_list = []
        for yr in range(1999, 2017):
            total = state_total(state, str(yr))
            xytuple = [yr, int(total)]
            #print(f"{xytuple[0]}, {xytuple[1]}\n")
            totals_list.append(xytuple)


        #Get the top 10 deaths for that state and year
        result = print_state(state, year)
        result_list = [result, totals_list, state]
        #result_and_coordinates = f"Clicked at ({x}, {y})\n" + result
        return result_list
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"


if __name__ == '__main__':
    app.run(debug=True, port=8000)
