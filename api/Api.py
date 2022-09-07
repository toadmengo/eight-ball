from flask_restful import Api, Resource, reqparse, request
from .request.cohere import predict

class APIHandler(Resource):
    def get(self):
        print("Log2")
        question = request.args.get("question")
        print("Log3")
        r = predict(question) 
        return {
            'resultStatus': 'SUCCESS',
            'message': "{}".format(r)
        }
        