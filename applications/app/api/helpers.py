from functools import wraps
from flask import session, jsonify

def login_required(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        if session.get('user_id', None):
            return f(*args, **kwargs)
        else:
            response = jsonify(message = 'Unauthorized user, please re-login to system.', status = 401)
            return response
    return wrapped
