from sys import path
from flask import Flask,request
from flask_restful import Resource, Api
from modules.api.convert_degrees import ConvertDegrees
from modules.api.search_post_code import SearchPostCode

app = Flask(__name__)
api = Api(app)

api.add_resource(ConvertDegrees, '/converte', methods=['POST'])
api.add_resource(SearchPostCode, '/consulta-cep', methods=['GET'])

if __name__ == "__main__":
    app.run()