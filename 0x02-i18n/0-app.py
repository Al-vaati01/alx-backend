#!/usr/bin/env python3
"""
Simple Flask i18n App
This script creates a basic internationalization (i18n) web
application using Flask
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello() -> str:
    """home"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(port=3000)
