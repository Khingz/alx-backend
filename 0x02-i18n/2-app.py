#!/usr/bin/env python3
"""A simple flask app
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """Comments"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@babel.localeselector
def get_locale():
    """Comment"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def hello_world():
    """_summary_
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
