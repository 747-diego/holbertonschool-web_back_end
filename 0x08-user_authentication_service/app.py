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
def emailCheck() -> str:
    """Email-Verification."""
    form_data = request.form
    if "email" not in form_data:
        return (jsonify({"message": "email required"}), 400)
    elif "password" not in form_data:
        return (jsonify({"message": "password required"}), 400)
    else:
        email = request.form.get("email")
        password = request.form.get("password")
        try:
            new_user = AUTH.register_user(email, password)
            return (jsonify({
                "email": new_user.email,
                "message": "user created"
            }))
        except ValueError:
            return (jsonify({"message": "email already registered"}), 400)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
