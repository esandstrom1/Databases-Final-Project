# app.py
from flask import Flask, render_template, request

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

if __name__ == '__main__':
    app.run(debug=True)
