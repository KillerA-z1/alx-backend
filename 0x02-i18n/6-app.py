#!/usr/bin/env python3
"""Flask app with user login mock and Babel integration."""


from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Optional


app = Flask(__name__)

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Configuration for Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


def get_user() -> Optional[dict]:
    """Retrieve a user based on the login_as URL parameter."""
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """Set user in global g if logged in."""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Determine the best match with supported languages."""
    # 1. Locale from URL parameters
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    # 2. Locale from user settings
    user = g.get('user')
    if user:
        user_locale = user.get('locale')
        if user_locale and user_locale in app.config['LANGUAGES']:
            return user_locale
    # 3. Locale from request header
    locale = request.accept_languages.best_match(app.config['LANGUAGES'])
    if locale:
        return locale
    # 4. Default locale
    return app.config['BABEL_DEFAULT_LOCALE']


@app.route('/')
def index():
    """Render the index template."""
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run()
