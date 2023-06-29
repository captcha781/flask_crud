from flask import Flask, jsonify, request
from flask_cors import CORS
from config.config import config
from routes.routes import bp as routes_app
from routes.auth_routes import abp as auth_routes_app

app = Flask(__name__)
CORS(app, methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'], origins='http://127.0.0.1:5500')

app.register_blueprint(routes_app, name='crud_routes')
app.register_blueprint(auth_routes_app, name='auth_routes')

if __name__ == '__main__':
    app.run(debug=config["debug"], port=config["port"])
