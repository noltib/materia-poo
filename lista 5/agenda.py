import datetime

class Contato:
    def __init__(self, i: int, n: str, e: str, f: str, d: datetime.datetime):
        self.id = i
        self.nome = n
        self.email = e
        self.fone = f
        self.nascimento = d

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Nome: {self.nome}\n"
            f"Email: {self.email}\n"
            f"Fone: {self.fone}\n"
            f"Nascimento: {self.nascimento.strftime('%d/%m/%Y')}\n"
        )

class ContatoUI:
    contatos = []

    @staticmethod
    def main():
        while True:
            op = ContatoUI.menu()
            if op == 1:
                ContatoUI.inserir()
            elif op == 2:
                ContatoUI.listar()
            elif op == 3:
                ContatoUI.atualizar()
            elif op == 4:
                ContatoUI.excluir()
            elif op == 5:
                ContatoUI.pesquisar()
            elif op == 6:
                ContatoUI.aniversariantes()
            elif op == 7:
                print("Encerrando programa.")
                break
            else:
                print("Opção inválida!")

    @staticmethod
    def menu():
        print("\n--- MENU AGENDA ---")
        print("1 - Inserir contato")
        print("2 - Listar contatos")
        print("3 - Atualizar contato")
        print("4 - Excluir contato")
        print("5 - Pesquisar por nome")
        print("6 - Aniversariantes do mês")
        print("7 - Sair")
        return int(input("Digite sua opção: "))

    @staticmethod
    def inserir():
        try:
            i = int(input("ID: "))
            n = input("Nome: ")
            e = input("Email: ")
            f = input("Fone: ")
            d = datetime.datetime.strptime(input("Nascimento (DD/MM/AAAA): "), "%d/%m/%Y")
            c = Contato(i, n, e, f, d)
            ContatoUI.contatos.append(c)
            print("Contato inserido com sucesso.")
        except:
            print("Erro ao inserir contato.")

    @staticmethod
    def listar():
        if not ContatoUI.contatos:
            print("Nenhum contato cadastrado.")
        else:
            for c in ContatoUI.contatos:
                print(c)

    @staticmethod
    def atualizar():
        try:
            i = int(input("Digite o ID do contato a atualizar: "))
            for c in ContatoUI.contatos:
                if c.id == i:
                    print("Contato encontrado. Digite os novos dados:")
                    c.nome = input("Nome: ")
                    c.email = input("Email: ")
                    c.fone = input("Fone: ")
                    c.nascimento = datetime.datetime.strptime(input("Nascimento (DD/MM/AAAA): "), "%d/%m/%Y")
                    print("Contato atualizado.")
                    return
            print("Contato não encontrado.")
        except:
            print("Erro ao atualizar.")

    @staticmethod
    def excluir():
        try:
            i = int(input("Digite o ID do contato a excluir: "))
            for c in ContatoUI.contatos:
                if c.id == i:
                    ContatoUI.contatos.remove(c)
                    print("Contato excluído.")
                    return
            print("Contato não encontrado.")
        except:
            print("Erro ao excluir.")

    @staticmethod
    def pesquisar():
        nome = input("Digite o nome para buscar: ").lower()
        achou = False
        for c in ContatoUI.contatos:
            if nome in c.nome.lower():
                print(c)
                achou = True
        if not achou:
            print("Nenhum contato encontrado com esse nome.")

    @staticmethod
    def aniversariantes():
        try:
            mes = int(input("Digite o número do mês (1 a 12): "))
            encontrados = [c for c in ContatoUI.contatos if c.nascimento.month == mes]
            if not encontrados:
                print("Nenhum aniversariante neste mês.")
            else:
                print("Aniversariantes do mês:")
                for c in encontrados:
                    print(f"{c.nome} - {c.nascimento.strftime('%d/%m')}")
        except:
            print("Entrada inválida.")
ContatoUI.main()