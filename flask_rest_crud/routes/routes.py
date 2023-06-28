from flask import jsonify, Blueprint
from flask_rest_crud.controller import crud_controller
from flask_rest_crud.middlewares.auth_middleware import token_validation

bp = Blueprint('routes', __name__)


@bp.route('/')
@token_validation
def home(resp):
    return jsonify({"app": "works fine!!!"})


@bp.route('/crud', methods=['GET'])
@token_validation
def read_crud(resp):
    return crud_controller.read_data()


@bp.route('/crud', methods=['POST'])
@token_validation
def write_crud(resp):
    return crud_controller.write_data()


@bp.route('/crud/<string:crud_id>', methods=['GET'])
@token_validation
def fetch_one_crud(resp, crud_id):
    return crud_controller.fetch_one_data(crud_id)


@bp.route('/crud/<string:crud_id>', methods=['PUT'])
@token_validation
def update_one_crud(resp, crud_id):
    return crud_controller.update_one_data(crud_id)


@bp.route('/crud/<string:crud_id>', methods=['DELETE'])
@token_validation
def delete_one_crud(resp, crud_id):
    return crud_controller.delete_one_data(crud_id)
