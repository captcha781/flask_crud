from flask import jsonify, Blueprint
from controller import auth_controller
from middlewares.auth_middleware import token_validation

abp = Blueprint('routes', __name__)


@abp.route('/signup', methods=['POST'])
@token_validation
def auth_signup(resp):
    if resp != 'passive':
        return jsonify({"success": False, "message": "Something went wrong"}), 500
    return auth_controller.signup()


@abp.route('/signin', methods=['POST'])
@token_validation
def auth_signin(resp):
    if resp != 'passive':
        return jsonify({"success": False, "message": "Something went wrong"}), 500
    return auth_controller.signin()
