from flask import Flask
from flask import jsonify


app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return """<h1>Welcome to my first website!!!<h1>"""

@app.route('/name/<value>')
def name(value):
    val = {"value": value}
    return jsonify(val)

@app.route('/html')
def html():
    """Returns some custom HTML"""
    return """
    <title>This is a Hello World World Page</title>
    <h1>Hello</h1>
    <p><b>World</b></p>
    """

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
