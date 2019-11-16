from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/heartbeat')
def test():
    return "Hello World"

@app.route('/test-input')
def test_input():
    name = request.args.get("name", "test")
    return "Hello, " + name

if __name__ == '__main__':
    app.run()