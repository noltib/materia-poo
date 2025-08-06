# ui.py

from contato import Contato, ContatoDAO
from view import View

class UI:
    def __init__(self):
        self.dao = ContatoDAO()

    def menu(self):
        print("\n1 - Inserir\n2 - Listar\n3 - Buscar por ID\n4 - Atualizar\n5 - Excluir")
        print("6 - Pesquisar por Iniciais\n7 - Aniversariantes do Mês")
        print("8 - Salvar\n9 - Carregar\n0 - Sair")
        return input("Escolha: ")

    def executar(self):
        self.dao.carregar()
        while True:
            op = self.menu()
            if op == "1":
                id = input("ID: ")
                nome = input("Nome: ")
                email = input("Email: ")
                telefone = input("Telefone: ")
                nascimento = input("Nascimento (AAAA-MM-DD): ")
                self.dao.inserir(Contato(id, nome, email, telefone, nascimento))
            elif op == "2":
                View.mostrar_lista(self.dao.listar())
            elif op == "3":
                id = input("ID: ")
                contato = self.dao.buscar_por_id(id)
                if contato:
                    View.mostrar_contato(contato)
                else:
                    print("Contato não encontrado.")
            elif op == "4":
                id = input("ID: ")
                c = self.dao.buscar_por_id(id)
                if c:
                    c.set_nome(input("Novo nome: "))
                    c.set_email(input("Novo email: "))
                    c.set_telefone(input("Novo telefone: "))
                    c.set_nascimento(input("Nova data nascimento (AAAA-MM-DD): "))
                else:
                    print("Contato não encontrado.")
            elif op == "5":
                id = input("ID a excluir: ")
                self.dao.excluir(id)
            elif op == "6":
                iniciais = input("Iniciais: ")
                View.mostrar_lista(self.dao.pesquisar_por_iniciais(iniciais))
            elif op == "7":
                mes = input("Mês (MM): ")
                View.mostrar_lista(self.dao.aniversariantes(mes))
            elif op == "8":
                self.dao.salvar()
            elif op == "9":
                self.dao.carregar("contatos.json")
            elif op == "0":
                break

if __name__ == "__main__":
    ui = UI()
    ui.executar()
