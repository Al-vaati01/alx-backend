#!/usr/bin/env python3
from flask import Flask, render_template, request, globals
from flask_babel import Babel
import pytz


app = Flask(__name__)


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    locale = request.args.get('locale')
    userl = globals.g.get(request.args.get('login_as')).get('locale')
    bestl = request.accept_languages.best_match(app.config['LANGUAGES'])

    if locale and locale in app.config['LANGUAGES']:
        return locale
    elif userl and userl in app.config['LANGUAGES']:
        return userl
    elif bestl and bestl in app.config['LANGUAGES']:
        request.accept_languages.best_match(app.config['LANGUAGES'])
    return app.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone():
    tz = request.args.get('timezone')
    usertz = globals.g.get(request.args.get('login_as')).get('timezone')

    if tz:
        if pytz.timezone(tz):
            return tz
        raise pytz.exceptions.UnknownTimeZoneError
    elif usertz:
        if pytz.timezone(usertz):
            return usertz
        raise pytz.exceptions.UnknownTimeZoneError
    return app.config['BABEL_DEFAULT_TIMEZONE']


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    login_as = request.args.get('login_as')
    if not login_as and login_as not in users.keys():
        return None
    return users.get(int(login_as))


@app.before_request
def before_request():
    globals.g.setdefault(request.args.get('login_as'), get_user())


@app.route("/")
def hello():
    user = globals.g.get(request.args.get('login_as'))
    username = user.get('name')
    return render_template('7-index.html',
                           username=username,
                           timezone=get_timezone())


if __name__ == '__main__':
    app.run(port=4000)
