#!/bin/env python3
"""User-Authentication."""


import bcrypt
import uuid
from bcrypt import checkpw
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """Turn string arguments and returns bytes."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def _generate_uuid() -> str:
    """String-representation of new UUID."""
    return (str(uuid.uuid4()))


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        """Init."""
        self._db = DB()

    def sign_up(self, email: str, password: str) -> User:
        """Sign up and create account."""
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {email} already exists")
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

    def check_password(self, email: str, password: str) -> bool:
        """If email exists check pasword."""
        try:
            found_user = self._db.find_user_by(email=email)
            return (checkpw(
                password.encode('utf-8'),
                found_user.hashed_password
                ))
        except NoResultFound:
            return (False)

    def create_session(self, email: str) -> str:
        """Get session ID."""
        session_id = _generate_uuid()
        try:
            user = self._db.find_user_by(email=email)
            self._db.update_user(user.id, session_id=session_id)
            return (session_id)
        except NoResultFound:
            return (None)

    def sign_in(self, email: str, password: str) -> bool:
        """Username works."""
        try:
            username = self._db.find_user_by(email=email)
            if checkpw(password.encode(), username.hashed_password):
                return (True)
        except NoResultFound:
            pass
        return (False)

    def get_user_from_session_id(self, session_id: str) -> str:
        """Single session string."""
        try:
            username = self._db.find_user_by(session_id=session_id)
            return (username.email + ":" + str(username.id))
        except NoResultFound:
            return (None)

    def destroy_session(self, user_id: int) -> None:
        """Take a single id integer argument and returns None."""
        try:
            username = self._db.find_user_by(id=user_id)
            self._db.update_user(user_id, session_id=None)
            return (None)
        except NoResultFound:
            return (None)
