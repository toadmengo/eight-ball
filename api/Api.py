from flask_restful import Api, Resource, reqparse
from .request.cohere import predict

class APIHandler(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('question')
        args = parser.parse_args()
        question = args["question"]
        r = predict(question) 
        return {
            'resultStatus': 'SUCCESS',
            'message': "{}".format(r)
        }
        