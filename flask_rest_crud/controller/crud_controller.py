from flask import request, jsonify
from database.db import Database

db = Database()


def read_data():
    try:
        print(request.path)
        data = db.find_many("crud", {})
        return jsonify({"data": data})
    except:
        return jsonify({"success": False, "message": "Something went wrong"}), 500


def write_data():
    try:
        req_body = request.get_json()
        data = db.insert_one("crud", req_body).inserted_id
        if data:
            return jsonify({"success": True, "message": "Data inserted successfully"})
    except:
        return jsonify({"success": False, "message": "Something went wrong"}), 500


def fetch_one_data(crud_id):
    try:
        data = db.find_one_by_id("crud", crud_id)

        if not data:
            return jsonify({"success": False, "message": "Cannot find the matching data"}), 400
        else:
            return jsonify({"success": True, "message": "Found matching data", "data": data}), 200
    except:
        return jsonify({"success": False, "message": "Something went wrong"}), 500

def update_one_data(crud_id):
    try:
        req_body = request.get_json()
        updation_data = db.update_one_by_id("crud", crud_id, req_body)
        if not updation_data['status']:
            return jsonify({"success": False, "message": updation_data['message']}), 400
        else:
            return jsonify({"success": True, "message": updation_data['message']}), 200

    except:
        return jsonify({"success": False, "message": "Something went wrong"}), 500


def delete_one_data(crud_id):
    try:
        deletion_data = db.delete_one_by_id('crud', crud_id)
        if not deletion_data['status']:
            return jsonify({"success": False, "message": deletion_data['message']}), 400
        else:
            return jsonify({"success": True, "message": deletion_data['message']}), 200

    except:
        return jsonify({"success": False, "message": "Something went wrong"}), 500