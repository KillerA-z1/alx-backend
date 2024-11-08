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

from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Determine the best match with our supported languages.

    This function uses request.accept_languages to determine the best match
    with the supported languages defined in the app configuration.

    Returns:
        str: The best match for the supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Render the index.html template with translated messages.

    This function renders the 3-index.html template, passing translated strings
    for home_title and home_header.

    Returns:
        str: The rendered HTML template.
    """
    return render_template('3-index.html',
                           home_title=gettext('home_title'),
                           home_header=gettext('home_header'))


if __name__ == '__main__':
    app.run()
