# app/decorators.py

from functools import wraps
from typing import Optional

from flask import g, redirect, url_for, jsonify


def login_required(redirect_to_login: Optional[bool] = False):
    """
    Decorator that ensures the user is authenticated before accessing the route.
    If the user is not authenticated, it redirects to the login page or returns a 401 error.
    """

    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not getattr(g, 'corbado_user', None):
                if redirect_to_login:
                    return redirect(url_for('login'))
                else:
                    # Return a JSON error message with a 401 status code
                    response = {
                        'error': 'Unauthorized',
                        'message': 'Please log in to access this resource.'
                    }
                    return jsonify(response), 401
            return f(*args, **kwargs)

        return decorated_function

    return decorator


def require_unauthenticated():
    """
    Decorator factory that ensures the user is not authenticated before accessing the route.
    If the user is authenticated, it redirects to the profile page.
    """

    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if getattr(g, 'corbado_user', None):
                return redirect(url_for('profile'))
            return f(*args, **kwargs)

        return decorated_function

    return decorator
