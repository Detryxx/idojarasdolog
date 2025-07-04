from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask API tutorial!"

@app.route('/api/data')
def get_data():
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
        # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        response.raise_for_status()  
        data = response.json()
    except requests.exceptions.HTTPError as http_err:
        return jsonify({'error': f'HTTP error occurred: {http_err}'}), 500
    except Exception as err:
        return jsonify({'error': f'Other error occurred: {err}'}), 500
    return render_template('data.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)