from flask_restful import Resource, Api

class Firstapi(Resource):
    def get(self):
        return {'Hello':'world!!!'}

