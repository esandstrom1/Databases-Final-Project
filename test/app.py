# app.py
from flask import Flask, render_template, request, jsonify
import sqlite3


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process_click', methods=['POST'])
def process_click():
    data = request.get_json()
    x = data['x']
    y = data['y']
    # Call your Python function with the x and y coordinates
    result = your_function(x, y)
    return {'result': result}


def your_function(x, y):
    # Your Python logic based on the clicked coordinates
    # Replace this with your actual functionality
    return f"Clicked at ({x}, {y})"


def test_query():
    conn = sqlite3.connect('causes.db')
    cursor = conn.cursor()

    query = f"SELECT Cause_Name, Deaths, Year FROM DATA WHERE Cause_Name != 'All causes' ORDER BY Deaths DESC LIMIT {5}"
    
    # Fetch all results from the query
    result = cursor.fetchall()

    # Convert the query result to a JSON-serializable format
    # For example, convert the result to a list of dictionaries
    columns = [col[0] for col in cursor.description]  # Get column names
    json_result = []
    for row in result:
        json_result.append(dict(zip(columns, row)))

    # Serialize the JSON data
    serialized_data = json.dumps(json_result)

    # Close the database connection
    conn.close()

    return serialized_data


if __name__ == '__main__':
    app.run(debug=True)
