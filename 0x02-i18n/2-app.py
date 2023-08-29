#!/usr/bin/env python3
from flask import Flask
from flask import render_template
from flask_babel import Babel
from flask import request

app = Flask(__name__)


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUANGES'])


@app.route("/")
def hello():
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(port=3000)
