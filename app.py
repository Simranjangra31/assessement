from flask import Flask, jsonify, request

# Create Flask app
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to my Flask app running on port 5001!, Try to solve your equation"})

# Example route for addition
@app.route('/add', methods=['GET'])
def add():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    result = a + b
    return jsonify({"a": a, "b": b, "sum": result})

# Run app on port 5001
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
