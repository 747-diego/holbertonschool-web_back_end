#!/usr/bin/env python3
"""Encrypting passwords."""
import bcrypt


def hash_password(password: str) -> bytes:
    """A-salted, hashed password, which is a byte string."""
    UTF = 'utf8'
    PWencode = password.encode()
    SaltyString = bcrypt.gensalt()
    password = bcrypt.hashpw(PWencode(UTF), SaltyString)
    return(password)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Password Validation."""
    UTF = 'utf8'
    PWencode = password.encode()
    ValidatedHash = hashed_password
    password = bcrypt.checkpw(PWencode(UTF), ValidatedHash)
    return(password)
