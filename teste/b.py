import json

dados = {
    "nome": "Pedro",
    "idade": 35,
    "cidade": "Belo Horizonte"
}

string_json = json.dumps(dados)
print(dados)
print(string_json)