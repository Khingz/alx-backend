#!/usr/bin/env python3
"""A simple flask app
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config(object):
    """Comments"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Comment
    """
    _id = request.args.get('login_as')
    if _id:
        return users.get(int(_id))
    return None


@app.before_request
def before_request() -> None:
    """comment
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Comment"""
    local = request.args.get('locale')
    if local in app.config['LANGUAGES']:
        print(local)
        return local
    if g.user:
        local = g.user.get('locale')
        if local and local in app.config['LANGUAGES']:
            return locale
    local = request.headers.get('locale', None)
    if local in app.config['LANGUAGES']:
        return local
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello_world():
    """_summary_
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
