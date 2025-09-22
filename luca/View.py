# I. Desenvolver em Python um cadastro de contato usando programação em camadas:
from Model import ContatoDAO

class View:
    @staticmethod
    def Contato_inserir(contato):
        x = ContatoDAO
        return x.inserir(contato)
    @staticmethod
    def Contato_listar():
        x = ContatoDAO
        return x.listar()
    @staticmethod
    def Contato_listar_id(id):
        x = ContatoDAO
        return x.listar_id(id)
    @staticmethod
    def Contato_atualizar():
        x = ContatoDAO
        return x.atualizar()
    @staticmethod
    def Contato_excluir():
        x = ContatoDAO
        return x.excluir()
    @staticmethod
    def Contato_pesquisar():
        x = ContatoDAO
        return x.pesquisar()
    @staticmethod
    def Contato_aniversariantes():
        x = ContatoDAO
        return x.aniversariantes()