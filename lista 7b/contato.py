# contato.py

import json

class Contato:
    def __init__(self, id, nome, email, telefone, nascimento):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
        self.__nascimento = nascimento

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_telefone(self): return self.__telefone
    def get_nascimento(self): return self.__nascimento

    def set_nome(self, nome): self.__nome = nome
    def set_email(self, email): self.__email = email
    def set_telefone(self, telefone): self.__telefone = telefone
    def set_nascimento(self, nascimento): self.__nascimento = nascimento

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__telefone} - {self.__nascimento}"


class ContatoDAO:
    def __init__(self):
        self.__contatos = []

    def inserir(self, contato):
        self.__contatos.append(contato)

    def listar(self):
        return self.__contatos

    def buscar_por_id(self, id):
        for c in self.__contatos:
            if c.get_id() == id:
                return c
        return None

    def excluir(self, id):
        c = self.buscar_por_id(id)
        if c:
            self.__contatos.remove(c)

    def pesquisar_por_iniciais(self, iniciais):
        return [c for c in self.__contatos if c.get_nome().startswith(iniciais)]

    def aniversariantes(self, mes):
        return [c for c in self.__contatos if c.get_nascimento()[5:7] == mes]

    def salvar(self):
        with open("contatos.json", "w", encoding="utf-8") as f:
            json.dump([{
                "_Contato__id": c.get_id(),
                "_Contato__nome": c.get_nome(),
                "_Contato__email": c.get_email(),
                "_Contato__telefone": c.get_telefone(),
                "_Contato__nascimento": c.get_nascimento()
            } for c in self.__contatos], f, indent=4)


    def carregar(self):
        try:
            with open("contatos.json", "r", encoding="utf-8") as f:
                dados = json.load(f)
                self.__contatos = [
                    Contato(d["_Contato__id"], d["_Contato__nome"], d["_Contato__email"],
                            d["_Contato__telefone"], d["_Contato__nascimento"])
                    for d in dados
                ]
        except FileNotFoundError:
            self.__contatos = []

