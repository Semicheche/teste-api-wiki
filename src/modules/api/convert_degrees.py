from flask_restful import Resource
from flask import request
from modules.degrees.degrees import Degrees

class ConvertDegrees(Resource):

    def post(self):
        degress = Degrees()
        data = request.get_json()

        return degress.convert_degrees(data)

