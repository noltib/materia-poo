from datetime import datetime
from model import Contato, ContatoDAO
from view import View


class UI:
    contatos = []

    @staticmethod
    def main():
        UI.abrir()
        while True:
            op = View.menu()
            if op == 0: break
            elif op == 1:
                UI.inserir()
            elif op == 2:
                UI.listar()
            elif op == 3:
                UI.listar_id()
            elif op == 4:
                UI.atualizar()
            elif op == 5:
                UI.excluir()
            elif op == 6:
                UI.pesquisar()
            elif op == 7:
                UI.aniversariantes()
            elif op == 8:
                UI.abrir()
            elif op == 9:
                UI.salvar()

    @staticmethod
    def inserir():
        i = int(input("ID: "))
        n = input("Nome: ")
        e = input("E-mail: ")
        f = input("Telefone: ")
        d = datetime.strptime(input("Nascimento (dd/mm/aaaa): "), "%d/%m/%Y")
        datetime.strftime
        UI.contatos.append(Contato(i, n, e, f, d))

    @staticmethod
    def listar():
        for c in UI.contatos:
            print(c)
            print("-" * 20)

    @staticmethod
    def listar_id():
        id_buscado = int(input("ID do contato: "))
        for c in UI.contatos:
            if c.get_id() == id_buscado:
                print(c)
                return
        print("Contato não encontrado.")

    @staticmethod
    def atualizar():
        id_buscado = int(input("ID do contato a atualizar: "))
        for c in UI.contatos:
            if c.get_id() == id_buscado:
                c.set_nome(input("Novo nome: "))
                c.set_email(input("Novo e-mail: "))
                c.set_fone(input("Novo telefone: "))
                d = datetime.strptime(input("Nova data de nascimento (dd/mm/aaaa): "), "%d/%m/%Y")
                c.set_nascimento(d)
                return
        print("Contato não encontrado.")

    @staticmethod
    def excluir():
        id_buscado = int(input("ID do contato a excluir: "))
        UI.contatos = [c for c in UI.contatos if c.get_id() != id_buscado]

    @staticmethod
    def pesquisar():
        inicial = input("Digite as iniciais do nome: ").lower()
        encontrados = [c for c in UI.contatos if c.get_nome().lower().startswith(inicial)]
        for c in encontrados:
            print(c)
            print("-" * 20)
        if not encontrados:
            print("Nenhum contato encontrado.")

    @staticmethod
    def aniversariantes():
        mes = int(input("Digite o mês (1-12): "))
        encontrados = [c for c in UI.contatos if c.get_nascimento().month == mes]
        for c in encontrados:
            print(c)
            print("-" * 20)
        if not encontrados:
            print("Nenhum aniversariante nesse mês.")

    @staticmethod
    def abrir():
        UI.contatos = ContatoDAO.abrir()

    @staticmethod
    def salvar():
        ContatoDAO.salvar(UI.contatos)


ui = UI
ui.main()
