from datetime import datetime
import json

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

class ContatoUI:
    contatos = []

    @staticmethod
    def main():
        ContatoUI.abrir()
        while True:
            op = ContatoUI.menu()
            if op == 0: break
            elif op == 1:
                ContatoUI.inserir()
            elif op == 2:
                ContatoUI.listar()
            elif op == 3:
                ContatoUI.listar_id()
            elif op == 4:
                ContatoUI.atualizar()
            elif op == 5:
                ContatoUI.excluir()
            elif op == 6:
                ContatoUI.pesquisar()
            elif op == 7:
                ContatoUI.aniversariantes()
            elif op == 8:
                ContatoUI.abrir()
            elif op == 9:
                ContatoUI.salvar()

    @staticmethod
    def menu():
        print("\n--- MENU ---")
        print("1. Inserir")
        print("2. Listar todos")
        print("3. Listar por ID")
        print("4. Atualizar")
        print("5. Excluir")
        print("6. Pesquisar por nome")
        print("7. Aniversariantes do mês")
        print("8. Abrir arquivo")
        print("9. Salvar arquivo")
        print("0. Sair")
        op = int(input("Opção: "))
        return op

    @staticmethod
    def inserir():
        i = int(input("ID: "))
        n = input("Nome: ")
        e = input("E-mail: ")
        f = input("Telefone: ")
        d = datetime.strptime(input("Nascimento (dd/mm/aaaa): "), "%d/%m/%Y")
        ContatoUI.contatos.append(Contato(i, n, e, f, d))

    @staticmethod
    def listar():
        for c in ContatoUI.contatos:
            print(c)
            print("-" * 20)

    @staticmethod
    def listar_id():
        id_buscado = int(input("ID do contato: "))
        for c in ContatoUI.contatos:
            if c.get_id() == id_buscado:
                print(c)
                return
        print("Contato não encontrado.")

    @staticmethod
    def atualizar():
        id_buscado = int(input("ID do contato a atualizar: "))
        for c in ContatoUI.contatos:
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
        ContatoUI.contatos = [c for c in ContatoUI.contatos if c.get_id() != id_buscado]

    @staticmethod
    def pesquisar():
        inicial = input("Digite as iniciais do nome: ").lower()
        encontrados = [c for c in ContatoUI.contatos if c.get_nome().lower().startswith(inicial)]
        for c in encontrados:
            print(c)
            print("-" * 20)
        if not encontrados:
            print("Nenhum contato encontrado.")

    @staticmethod
    def aniversariantes():
        mes = int(input("Digite o mês (1-12): "))
        encontrados = [c for c in ContatoUI.contatos if c.get_nascimento().month == mes]
        for c in encontrados:
            print(c)
            print("-" * 20)
        if not encontrados:
            print("Nenhum aniversariante nesse mês.")

    @staticmethod
    def abrir():
        try:
            with open("contatos.json", "r") as f:
                dados = json.load(f)
                ContatoUI.contatos = [Contato(d['id'], d['nome'], d['email'], d['fone'],
                                              datetime.strptime(d['nascimento'], "%Y-%m-%d")) for d in dados]
        except FileNotFoundError:
            ContatoUI.contatos = []

    @staticmethod
    def salvar():
        dados = [{
            'id': c.get_id(),
            'nome': c.get_nome(),
            'email': c.get_email(),
            'fone': c.get_fone(),
            'nascimento': c.get_nascimento().strftime("%Y-%m-%d")
        } for c in ContatoUI.contatos]
        with open("contatos.json", "w") as f:
            json.dump(dados, f, indent=4)

ContatoUI.main()
