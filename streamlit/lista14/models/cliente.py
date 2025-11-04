import json
from models.dao import DAO


class Cliente:
    def __init__(self, id, nome, email, fone, senha, foto):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_senha(senha)
        self.set_foto(foto)

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone
    def get_senha(self): return self.__senha
    def get_foto(self): return self.__foto

    def set_senha(self, senha):
        if senha == "": raise ValueError("Senha inválida")
        self.__senha = senha
    def set_id(self, id): self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome inválido")
        self.__nome = nome
    def set_email(self, email):
        if email == "": raise ValueError("Email inválido")
        self.__email = email
    def set_fone(self, fone):
        if fone == "": raise ValueError("Telefone inválido")
        self.__fone = fone
    def set_foto(self, foto):
        if foto == "":
            with open("models/foto.txt", "r") as image_file:
                image_data = image_file.read() 
                self.__foto = image_data
        else:
            self.__foto = foto

    def to_json(self):
        dic = {"id":self.__id, "nome":self.__nome, "email":self.__email,"fone":self.__fone, "senha":self.__senha, "foto":self.__foto}
        return dic
    @staticmethod
    def from_json(dic):
        return Cliente(dic["id"], dic["nome"], dic["email"], dic["fone"],dic["senha"], dic["foto"])
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"

class ClienteDAO(DAO):
    @classmethod
    def abrir(cls):
        cls._objetos = []
        try:
            with open("clientes.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Cliente.from_json(dic)
                    cls._objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls._objetos, arquivo, default = Cliente.to_json) 

