#!/usr/bin/env python3
"""Simple Flask i18n App
This script creates a basic internationalization (i18n) web application using
Flask,
a micro web framework for Python. The app defines a single route for the root
URL ("/"),
which renders an HTML template named '0-index.html'. This template can be
customized
for different languages or content.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello() -> str:
    """home"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(port=3000)
