# app.py
from flask import Flask, render_template, request
import subprocess
from user_query import print_state

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
    #result = result.replace('\n', '<br>')
    return {'result': result}

def your_function(x, y):
    # Your Python logic based on the clicked coordinates
    # Replace this with your actual functionality
    try:
        # Call the "query.py" program and capture its output
        #result = subprocess.check_output(["python3", "user_query.py"], universal_newlines=True)
        result = print_state("Alaska", 2001)
        #result = result.replace('\n', '<br>')
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

    return f"Clicked at ({x}, {y})"

if __name__ == '__main__':
    app.run(debug=True)
