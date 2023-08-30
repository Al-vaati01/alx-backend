#!/usr/bin/env python3
"""
simple flask i18n app
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
