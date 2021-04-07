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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """User ID for Session ID mandatory."""
        if session_id is None:
            return(None)
        if session_id is not str:
            return(None)
        id = self.user_id_by_session_id.get(session_id)
        return(id)

    def current_user(self, request=None):
        """User instance based on a cookie value."""
        SessionCookie = self.session_cookie(request)
        CookieID = self.user_id_for_session_id(SessionCookie)
        if type(CookieID) == dict:
            CookieID = CookieID["user_id"]
        UserID = User.get(CookieID)
        return(UserID)
