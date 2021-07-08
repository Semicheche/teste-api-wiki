
from requests import get
from flask import request, jsonify

class PostCode():

    def get_post_code(self, cep):
        url = f'https://api.postmon.com.br/v1/cep/{cep}'
        result = get(url)

        if result.status_code == 200:
            return self.format_data(result.json())
        else:
            return jsonify( error=f'Não Foi possivel consultar o CEP: {cep}', status_code=result.status_code)


    def format_data(self, result):
        return { "rua": result.get('logradouro'), "cidade":result['cidade'], "estado":result['estado'] }
