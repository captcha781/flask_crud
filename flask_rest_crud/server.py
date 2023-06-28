from flask import Flask, jsonify, request
from flask_cors import CORS
from config.config import config
from routes.routes import bp as routes_app

app = Flask(__name__)
CORS(app)

app.register_blueprint(routes_app)

if __name__ == '__main__':
    app.run(debug=config["debug"], port=config["port"])
