from flask_restful import Resource
from flask import request
from modules.post_code.post_code import PostCode

class SearchPostCode(Resource):

    def get(self):
        cep = request.args.get('cep')
        post_code = PostCode()

        return post_code.get_post_code(cep)
