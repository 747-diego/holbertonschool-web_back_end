#!/usr/bin/env python3
"""API session authentication module."""

from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """Session Authentication."""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Instance method that creates a Session ID."""
        if user_id is None:
            return(None)
        if user_id is not str:
            return(None)
        GeneratedSession = str(uuid.uuid4())
        self.user_id_by_session_id[GeneratedSession] = user_id
        return(GeneratedSession)
