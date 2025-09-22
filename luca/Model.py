# I. Desenvolver em Python um cadastro de contato usando programação em camadas:
from datetime import datetime
import json

class Contato:
    def __init__(self, id, nome, email, nascimento, fone):
        self.__nome = nome
        self.__id = id
        self.__email = email
        self.__fone = fone
        self.__nascimento = datetime.strptime(nascimento, "%Y-%m-%d")

    def set_nome(self, de):
        try:
            float(de)
            print("nome invalido")
        except:
            self.__nome = de
    def set_id(self, de):
        try:
            float(de)
            str(de)
            self.__id = de
        except:
            print("id invalida")
    def set_email(self, de):
        try:
            float(de)
            print("email invalido")
        except:
            self.__email = de
    def set_fone(self, de):
        try:
            float(de)
            print("fone invalido")
        except:
            self.__fone = de
    def set_nascimento(self, de):
        try:
            de = datetime.strptime(de, "%Y, %m, %d")
            self.__nascimento = datetime.date(de)
        except:
            print("nascimento invalido")

    def get_nome(self):
        return self.__nome
    def get_id(self):
        return self.__id
    def get_email(self):
        return self.__email
    def get_fone(self):
        return self.__fone
    def get_nascimento(self):
        return self.__nascimento

    def __str__(self):
        return (f'{self.__id} ,{self.__nome} , {self.__email}, {self.__fone}, {self.__nascimento}')
    
    def contato(self):
        x = {}
        x["id"] = self.__id    
        x["nome"] = self.__nome
        x["email"] = self.__email
        x["nascimento"] = str(self.__nascimento)
        x["fone"] = self.__fone
        return x

class ContatoDAO:
    __contatos = []
    @classmethod
    def inserir(ui, x):
        z = Contato(x[0], x[1], x[2], x[3], x[4])
        try: 
            ui.__abrir()
        except:
            pass
        ui.__contatos.append(z)
        ui.__salvar()

    @classmethod
    def listar(ui):
        ui.__abrir()
        return ui.__contatos
    
    @classmethod
    def listar_id(ui, z):
        ui.__abrir()
        for x in ui.__contatos:
            if x.get_id().startswith(z):
                return x

    @classmethod
    def atualizar(ui):
        ui.__abrir()
        for x in ui.__contatos:
            if x.get_id() == int(input("informe o id do contato que deseja atualizar:")):
                x.set_nome(input("nome"))
                x.set_email(input("email"))
                x.set_nascimento("nascimento")
                x.set_fone("fone")
                ui.__salvar()
                print("contato atualizado")
                return
            else: 
                print("id invalido")

    @classmethod
    def excluir(ui):
        ui.__abrir()
        y = input("informe o id do contato que deseja excluir:")
        for x in ui.__contatos:
            if x.get_id() == y:
                ui.__contatos.remove(x)
                ui.__salvar()

    @classmethod
    def pesquisar(ui):
        ui.__abrir()
        x = input("Informe o nome: ")
        for y in ui.__contatos:
            if y.get_nome().startswith(x):
                return y

    @classmethod
    def aniversariantes(ui):
        z = []
        y = input("Informe o mês")
        ui.__abrir()
        for x in ui.__contatos:
            if x.get_nascimento().month == y:
                z.append(x)
        return z
    @classmethod
    def __abrir(ui):
        with open("contatos2.json", mode="r") as arquivo:
            data = json.load(arquivo)

            for i in data:
                novo_contato = Contato(i["id"], i["nome"], i["email"], i["nascimento"], i["fone"])
                ui.__contatos.append(novo_contato)

    @classmethod
    def __salvar(ui):
        with open("contatos2.json", mode="w") as arquivo:
            json.dump(ui.__contatos, arquivo, default = Contato.contato)