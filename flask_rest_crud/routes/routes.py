from flask import jsonify, Blueprint
from flask_rest_crud.controller import crud_controller

bp = Blueprint('routes', __name__)


@bp.route('/')
def home():
    return jsonify({"app": "works fine!!!"})


@bp.route('/crud', methods=['GET'])
def read_crud():
    return crud_controller.read_data()


@bp.route('/crud', methods=['POST'])
def write_crud():
    return crud_controller.write_data()


@bp.route('/crud/<string:crud_id>', methods=['GET'])
def fetch_one_crud(crud_id):
    return crud_controller.fetch_one_data(crud_id)


@bp.route('/crud/<string:crud_id>', methods=['PUT'])
def update_one_crud(crud_id):
    return crud_controller.update_one_data(crud_id)


@bp.route('/crud/<string:crud_id>', methods=['DELETE'])
def delete_one_crud(crud_id):
    return crud_controller.delete_one_data(crud_id)
