#!/usr/bin/env python3
"""
A module: Defines an template class for all template
for all authentication system implemented in this application
"""
from flask import request

from typing import (
    List,
    TypeVar
)


class Auth:
    """
    API authentication class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Requires authentication on every request
        """
        if (
            path is None
            or excluded_paths is None
            or len(excluded_paths) == 0
        ):
            return True
        for url in excluded_paths:
            if url.endswith('*'):
                if url[:-1] in path:
                    return False
            else:
                if path in url or path + '/' in url:
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Extract authorization header
        """
        auth = request.headers.get('Authorization', None) if request else None
        if request is None or auth is None:
            return None
        return auth

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Holds the current authenticated logged in user
        """
        return None
