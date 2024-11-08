#!/usr/bin/env python3
"""
This module sets up a basic Flask application.

It imports the necessary Flask modules and initializes the Flask app.
The application registers a blueprint for routing and runs the server
on host 0.0.0.0 and port 5000.

Attributes:
    app (Flask): The Flask application instance.

Usage:
    To run the application, execute this script directly.
"""
from flask import Flask, render_template, Blueprint

app = Flask(__name__)

# Define the blueprint
app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/')
def index():
    """Render the index.html template."""
    return render_template('0-index.html')

# Register the blueprint with the Flask app
app.register_blueprint(app_routes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
