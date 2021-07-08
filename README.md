# teste-api-wiki

## API feito em Python/Flask para consultar o CEP via GET e para conversao de temperatura Celsius, Kelvin e Fahrenheit

#
 - Python 3.7.2
 - Flask 2.0.1

### o clone o repositorio
```
    $ git clone https://github.com/Semicheche/teste-api-wiki.git
```
### crie o ambiente virtual
```
    $ python3 -m venv venv
```
### Instale os requirements
```
   $ pip install -r requirements.txt
```

### Rodando o projeto
```
    $ python src/app.py
```

# Endpoints

## consultar CEP
  | Codigo HTTP |URL                                                  |
  |-------------|-----------------------------------------------------|
  |  GET        | http://localhost:5000/consulta-cep?cep=numero-cep |

### output
```
    { "rua": "<nome-rua>", "cidade": "<nome-cidade>", "estado": "<sigla>" }
```
## Conversao Temperatura
  | Codigo HTTP |URL                                                  |
  |-------------|-----------------------------------------------------|
  |  POST        | http://localhost:5000/converte                     |

### input
```
    { "UnidadeOrigem": "C", "UnidadeDestino": "F", "Valor": 22 }
```

### output
```
{ "ValorConvertido": 71.6 }
```



