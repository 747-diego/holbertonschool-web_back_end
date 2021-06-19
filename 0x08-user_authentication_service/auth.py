#!/bin/env python3
"""User Authentication."""
from db import DB
from user import User

from bcrypt import hashpw, gensalt, checkpw
from sqlalchemy.orm.exc import NoResultFound
from typing import Union
from uuid import uuid4


def _hash_password(password: str) -> str:
    """Turn string arguments and returns bytes."""
    return hashpw(password.encode('utf-8'), gensalt())
