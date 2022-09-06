from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
# from flask_cors import CORS #comment this on deployment
from api.Api import APIHandler

app = Flask(__name__, static_folder='ReactApp/build')
# CORS(app) #comment this on deployment
api = Api(app)

@app.route("/", defaults={'path':''})
def serve(path):
    print("Log1")
    print(send_from_directory(app.static_folder, 'index.html'))
    print("Log2")
    return send_from_directory(app.static_folder, 'index.html')

api.add_resource(APIHandler, '/ask')