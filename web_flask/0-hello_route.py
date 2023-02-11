i#!/usr/bin/python3
"""Starts Flask web app
Listening on 0.0.0.0:5000
Route '/' displays "Hello HBNB!"
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Start a basic Flask web application"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
