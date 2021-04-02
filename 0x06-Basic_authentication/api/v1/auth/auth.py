#!/usr/bin/env python3
"""Auth class."""

from flask import request
from typing import List, TypeVar


class Auth:
    """For all authentication system."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Public method."""
        if len(excluded_paths) == 0:
            return(True)
        if path is None:
            return(True)
        if excluded_paths is None:
            return(True)
        if path[-1] != '/':
            path = path + '/'
        if path in excluded_paths:
            return(False)
        else:
            return(True)

    def authorization_header(self, request=None) -> str:
        """Public method."""
        if "Authorization" not in request.headers:
            return(None)
        if request is None:
            return(None)
        else:
            return(request.headers.get('Authorization'))

    def current_user(self, request=None) -> TypeVar('User'):
        """Public method."""
        return(None)
