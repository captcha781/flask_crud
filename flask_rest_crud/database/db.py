from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId
from config.config import config
import json

client = MongoClient(config["db"]["uri"])
db = client[config['db']['name']]

class Database:
    def __init__(self):
        self.client = client
        self.db = db

    def insert_one(self, collection: str, data: any) -> object:
        insert_data = self.db[collection].insert_one(data)
        return insert_data

    def find_many(self, collection: str, condition: object, projection=None, sort=None, limit=0, cursor=False) -> any:
        found_data = self.db[collection].find(filter=condition, projection=projection, sort=sort, limit=limit)

        if cursor:
            return found_data

        found_data = list(found_data)
        for i in range(len(found_data)):
            if "_id" in found_data[i]:
                found_data[i]["_id"] = str(found_data[i]["_id"])
        return found_data

    def find_one_by_id(self, collection: str, obj_id: str):
        found_data = self.db[collection].find_one({"_id": ObjectId(obj_id)})

        if found_data is None:
            return False

        if '_id' in found_data:
            found_data["_id"] = str(found_data["_id"])

        return found_data

    def update_one_by_id(self, collection: str, obj_id: str, data):
        found_data = self.db[collection].find_one({"_id": ObjectId(obj_id)})
        if found_data is None:
            return {"status": False, "message": "No matching data found"}

        update_data = self.db[collection].update_one({"_id": ObjectId(obj_id)}, {'$set': data})

        if update_data.matched_count == 1:
            if update_data.modified_count == 1:
                return {"status": True, "message": "Modified successfully"}
            elif update_data.modified_count == 0:
                return {"status": True, "message": "No data has been modified"}
            else:
                return {"status": False, "message": "Error in updating data"}

    def delete_one_by_id(self, collection: str, obj_id: str):
        found_data = self.db[collection].find_one({"_id": ObjectId(obj_id)})
        if found_data is None:
            return {"status": False, "message": "No matching data found"}

        delete_data = self.db[collection].delete_one({"_id": ObjectId(obj_id)})
        if delete_data.deleted_count == 1:
            return {"status": True, "message": "Deleted successfully"}
        elif delete_data.deleted_count == 0:
            return {"status": False, "message": "No matching data deleted"}


class User:
    def __init__(self):
        self.client = client
        self.db = db

    def find_user_by_id(self, collection, obj_id):
        found_data = self.db[collection].find_one({"_id": ObjectId(obj_id)})

        if found_data is None:
            return {"status": False, "user": None}
        else:
            found_data["_id"] = str(found_data["_id"])
            return {"status": True, "user": found_data}

    def find_existing_email_username(self, collection, email, username):
        found_data_email = self.db[collection].find_one({"email": email})
        found_data_username = self.db[collection].find_one({"username": username})

        print(found_data_username)
        print(found_data_email)
        if found_data_email is None and found_data_username:
            return "username"
        elif found_data_email and found_data_username is None:
            return "email"
        elif found_data_email is not None and found_data_username is not None:
            return "email"
        elif found_data_email is None and found_data_username is None:
            return False

    def find_user_by_email(self, collection, email):
        found_data = self.db[collection].find_one({'email':email})

        if not found_data:
            return {'status': False, 'user': None}
        else:
            return {'status': True, 'user': found_data}

    def insert_user(self, collection, data):
        insert_data = self.db[collection].insert_one(data)
        return insert_data
