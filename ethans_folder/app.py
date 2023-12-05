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

        #result = result.replace('\n', '<br>')
        print(result)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

    return f"Clicked at ({x}, {y})"


# def test_query():
#     conn = sqlite3.connect('causes.db')
#     cursor = conn.cursor()

#     query = f"SELECT Cause_Name, Deaths, Year FROM DATA WHERE Cause_Name != 'All causes' ORDER BY Deaths DESC LIMIT {5}"
    
#     # Fetch all results from the query
#     result = cursor.fetchall()

#     # Convert the query result to a JSON-serializable format
#     # For example, convert the result to a list of dictionaries
#     columns = [col[0] for col in cursor.description]  # Get column names
#     json_result = []
#     for row in result:
#         json_result.append(dict(zip(columns, row)))

#     # Serialize the JSON data
#     serialized_data = json.dumps(json_result)

#     # Close the database connection
#     conn.close()

#     return serialized_data


if __name__ == '__main__':
    app.run(debug=True, port=8000)
