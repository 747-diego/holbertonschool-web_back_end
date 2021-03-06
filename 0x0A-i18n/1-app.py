#!/usr/bin/env python3
"""Basic Bebel Setup."""


from flask import Flask
from flask import render_template
from flask_babel import Babel
import os


class Config(object):
    """Babel Flask Configuration."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object('1-app.Config')
babel = Babel(app)


@app.route('/', methods=['GET'], strict_slashes=False)
def Basic_Flask():
    """Basic-Flask-App."""
    return(render_template('1-index.html'))


if __name__ == "__main__":
    IPaddress = os.getenv("API_HOST", "0.0.0.0")
    app.run(host=IPaddress, port='5000')
