from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
# from flask_cors import CORS #comment this on deployment
from api.Api import APIHandler

app = Flask(__name__, static_url_path='', static_folder='js/build')
# CORS(app) #comment this on deployment
api = Api(app)

@app.route("/", defaults={'path':''})
def serve(path):
    print("Log1")
    print(app.send_static_file('index.html'))
    print("Log2")
    return app.send_static_file('index.html')

api.add_resource(APIHandler, '/ask')