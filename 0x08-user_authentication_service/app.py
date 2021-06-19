#!/usr/bin/env python3
"""Basic-Flask-App."""

from flask import Flask, jsonify, request, abort, redirect, url_for
from sqlalchemy.orm.exc import NoResultFound

from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome() -> str:
    """Welcome-to-Flask."""
    return jsonify({"message": "Bienvenue"})

@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """ POST /users
    Registers new user with email and pswd in x-www-form-urlencoded request,
    or finds if user already registered based on email
    Return:
      - JSON payload
    """

    """ form-data uses request.form, body JSON uses request.get_json() """
    form_data = request.form

    if "email" not in form_data:
        return jsonify({"message": "email required"}), 400
    elif "password" not in form_data:
        return jsonify({"message": "password required"}), 400
    else:

        email = request.form.get("email")
        pswd = request.form.get("password")

        try:
            new_user = AUTH.register_user(email, pswd)
            return jsonify({
                "email": new_user.email,
                "message": "user created"
            })
        except ValueError:
            return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
