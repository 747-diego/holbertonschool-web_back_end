#!/bin/env python3
"""User Authentication."""
import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """ Hash a password """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

