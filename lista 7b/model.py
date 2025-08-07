from datetime import datetime

class Contato:
    def __init__(self, i, n, e, f, d):
        self.__id = i
        self.set_nome(n)
        self.set_email(e)
        self.set_fone(f)
        self.set_nascimento(d)

    def __str__(self):
        return (f"ID: {self.__id}\nNome: {self.__nome}\nE-mail: {self.__email}\nTelefone: {self.__fone}\nNascimento: {self.__nascimento.strftime('%d/%m/%Y')}")

    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_email(self):
        return self.__email
    def get_fone(self):
        return self.__fone
    def get_nascimento(self):
        return self.__nascimento

    def set_nome(self, nome):
        if nome:
            self.__nome = nome
        else:
            raise ValueError("o nome é obrigatorio")
    def set_email(self, email):
        if email:
            self.__email = email
        else:
            raise ValueError("o email é obrigatorio")
    def set_fone(self, fone):
        if fone:
            self.__fone = fone
        else:
            raise ValueError("o telefone é obrigatorio")
    def set_nascimento(self, nascimento):
        self.__nascimento = nascimento

import json

class ContatoDAO:
    @staticmethod
    def salvar(contatos):
        dados = [{
            'id': c.get_id(),
            'nome': c.get_nome(),
            'email': c.get_email(),
            'fone': c.get_fone(),
            'nascimento': c.get_nascimento().strftime("%Y-%m-%d")
        } for c in contatos]
        with open("contatos.json", "w") as f:
            json.dump(dados, f, indent=4)

    @staticmethod
    def abrir():
        try:
            with open("contatos.json", "r") as f:
                dados = json.load(f)
                contatos = []
                for d in dados:
                    contatos.append(Contato(
                        d['id'], d['nome'], d['email'], d['fone'],
                        datetime.strptime(d['nascimento'], "%Y-%m-%d")
                    ))
                return contatos
        except FileNotFoundError:
            return []
