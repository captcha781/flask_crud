from flask import request, jsonify
from database.db import User
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import os

db = User()


def signup():
    try:
        req_body = request.get_json()

        if not (req_body['email'] or req_body['password'] or req_body['confirmPassword'] or req_body['username']):
            return jsonify({"success": False, "message": "Please fill in all the fields"})

        find_email = db.find_existing_email_username('user', req_body['email'], req_body['username'])
        print(find_email)
        if find_email == 'username' or find_email == 'email':
            return jsonify({"success": False, "message": find_email + " already exists"}), 400

        if req_body['password'] != req_body['confirmPassword']:
            return jsonify({"success": False, "message": "Passwords doesn't match"})

        hashed_pass = generate_password_hash(req_body['password'], method="pbkdf2", salt_length=10)

        userinfo = {
            "email": req_body['email'],
            "password": hashed_pass,
            "username": req_body['username']
        }

        insert_user = db.insert_user('user', userinfo)

        if insert_user.inserted_id:
            return jsonify({'success': True, "message": "Registration successful"})
        else:
            return jsonify({'success': False, "message": "Registration failed"})
    except:
        return jsonify({'success': False, 'message': 'Something went wrong'})


def signin():
    try:

        req_body = request.get_json()

        if not (req_body['email'] or req_body['password']):
            return jsonify({"success": False, 'message': "Please fill in email and password fields correctly"}), 401

        userinfo = db.find_user_by_email('user', req_body['email'])

        if not userinfo['status']:
            return jsonify({'success': False, 'message': 'User not found'})
        userinfo['user']['_id'] = str(userinfo['user']['_id'])

        if not check_password_hash(userinfo['user']['password'], req_body['password']):
            return jsonify({'success': False, 'message': 'Incorrect password'})

        token = jwt.encode({'id': str(userinfo['user']['_id'])}, os.getenv('JWT_SECRET'))
        userinfo['user']['password'] = ''
        return jsonify({'success': True, 'message': 'Login successful', 'token': str(token), 'user': userinfo['user']})


    except:
        return jsonify({'success': False, 'message': 'Something went wrong'})
