#!/usr/bin/env python3
"""
This module sets up a Flask application with Babel for internationalization.

It imports the necessary Flask and Babel modules, initializes the Flask app,
and configures Babel for language support.

Attributes:
    app (Flask): The Flask application instance.
    babel (Babel): The Babel instance for internationalization.

Usage:
    To run the application, execute this script directly.
"""


from flask import Flask, render_template
from flask_babel import Babel, gettext


app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    return render_template('3-index.html',
                           home_title=gettext('home_title'),
                           home_header=gettext('home_header'))


if __name__ == '__main__':
    app.run()
