from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the API"

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})

@app.route('/greet/<name>', methods=['GET'])
def greet(name):
    return jsonify({"message": f"Hello, {name}!"})

@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.get_json()

    num1 = data.get('num1')
    num2 = data.get('num2')

    result = num1 + num2
    return jsonify({"num1": num1, "num2": num2, "result": result})

if __name__ == '__main__':
    app.run(debug=True)
