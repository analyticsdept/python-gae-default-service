from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Service classes

class Warmup(Resource):
    def get(self):
        return '', 200, {}

class Services(Resource):
    def get(self):
        return '', 200, {}

# Error handling

@app.errorhandler(404)
@app.errorhandler(401)
@app.errorhandler(500)
def probs(error_code):
    return str(error_code)

# Routes

api.add_resource(Services, '/')
api.add_resource(Warmup, '/_ah/warmup')