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
from flask_babel import Babel

app = Flask(__name__)


# Configure available languages and Babel
class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Determine the best match with supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Render the index template."""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
