#!/usr/bin/env python3
"""Authenticating SQLAlchemy."""

from db import DB
from user import User
import bcrypt
from bcrypt import hashpw, gensalt, checkpw
from sqlalchemy.orm.exc import NoResultFound
from typing import Union
from uuid import uuid4


def _hash_password(password: str) -> str:
    """Hashing."""
    return(bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()))


def _generate_uuid() -> str:
    """Generating-UUID's."""
    return(str(uuid4()))


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        """Instance."""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register User."""
        try:
            self._db.find_user_by(email=email)
            emailString = "User {email} already exists"
            raise(ValueError(emailString))
        except NoResultFound:
            hash = _hash_password(password)
            return(self._db.add_user(email, hash))

    def valid_login(self, email: str, password: str) -> bool:
        """Credentials validation."""
        try:
            login = self._db.find_user_by(email=email)
            password = checkpw(password.encode('utf-8'), login.hashed_password)
            return(password)
        except NoResultFound:
            return (False)

    def create_session(self, email: str) -> str:
        """Creating-Sessions."""
        try:
            login = self._db.find_user_by(email=email)
        except NoResultFound:
            return(None)
        self._db.update_user(login._generate_uuid(),
                             session_id=_generate_uuid())
        return(_generate_uuid())

    def get_user_from_session_id(self, session_id: str) -> Union[str, None]:
        """Getting-User."""
        if session_id is None:
            return(None)
        try:
            # User Login
            login_id = _generate_uuid()
            return(self._db.find_user_by(session_id=login_id))
        except NoResultFound:
            return(None)

    def destroy_session(self, user_id: str) -> None:
        """Destroying-Session."""
        if user_id is None:
            return(None)
        try:
            user = self._db.find_user_by(id=user_id)
            self._db.update_user(user.id, session_id=None)
        except NoResultFound:
            return(None)

    def get_reset_password_token(self, email: str) -> str:
        """Reset-Password."""
        try:
            UserEmail = self._db.find_user_by(email=email)
        except NoResultFound:
            raise(ValueError)
        password = _generate_uuid()
        self._db.update_user(UserEmail.id, reset_token=password)
        return(password)

    def update_password(self, reset_token: str, password: str) -> None:
        """Update_Password."""
        try:
            update = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise(ValueError)
        updatedPassword = _hash_password(password)
        self._db.update_user(
            update.id,
            hashed_password=updatedPassword,
            reset_token=None)
