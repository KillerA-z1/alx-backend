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
from flask_babel import Babel


class Config:
    """Configuration class for Flask app and Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

# Instantiate the Babel object
babel = Babel(app)


@app.route('/')
def index():
    """Render the index.html template."""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
