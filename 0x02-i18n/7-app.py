#!/usr/bin/env python3
"""Flask app with user login mock, Babel integration, and time zone selector"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Optional
import pytz
from pytz.exceptions import UnknownTimeZoneError


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
    """Retrieve a user based on the 'login_as' URL parameter."""
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """Set user in global 'g' before each request."""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Determine the best match for supported languages."""
    # 1. Locale from URL parameters
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    # 2. Locale from user settings
    user = g.get('user')
    if user:
        user_locale = user.get('locale')
        if user_locale in app.config['LANGUAGES']:
            return user_locale
    # 3. Locale from request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """Determine the appropriate time zone."""
    # 1. Timezone from URL parameters
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            pass
    # 2. Timezone from user settings
    user = g.get('user')
    if user:
        user_timezone = user.get('timezone')
        if user_timezone:
            try:
                pytz.timezone(user_timezone)
                return user_timezone
            except UnknownTimeZoneError:
                pass
    # 3. Default to UTC
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index():
    """Render the index template."""
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run()
