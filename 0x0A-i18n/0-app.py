#!/usr/bin/env python3
"""Basic Flask app."""
from flask import Flask, request, render_template
from os import getenv

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def Basic_Flask():
    """Basic-Flask-App."""
    return(render_template('0-index.html'))


if __name__ == "__main__":
    IPaddress = getenv("API_HOST", "0.0.0.0")
    app.run(host=IPaddress, port='5000')
