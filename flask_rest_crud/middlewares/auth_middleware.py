import jwt
from functools import wraps
from flask import request, jsonify
import os
from database.db import User

db = User()


def token_validation(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'authorization' in request.headers:
            token = request.headers['authorization']
        if not token and (request.path == '/signup' or request.path == '/signin'):
            return f("passive", *args, **kwargs)

        if not token:
            return jsonify({'success': False, 'message': 'Auth token not found'}), 401

        try:
            decoded = jwt.decode(str(token), str(os.getenv('JWT_SECRET')), verify=True, algorithms='HS256')
            current_user = db.find_user_by_id('user', decoded["id"])

        except:
            return jsonify({'success': False,'message': 'Invalid auth token'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

