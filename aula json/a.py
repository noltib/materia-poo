import json
class Cliente:
    def __init__(self, id, n, e, f):
        self.__id = id
        self.__nome = n
        self.__email = e
        self.__fone = f

    def __str__(self):
        return f"ID: {self.__id} | Nome: {self.__nome} | Email: {self.__email} | Fone: {self.__fone}"
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone

    def set_nome(self, nome): self.__nome = nome
    def set_email(self, email): self.__email = email
    def set_fone(self, fone): self.__fone = fone
    def to_dict(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "email": self.__email,
            "fone": self.__fone
        }

    def from_dict(d):
        return Cliente(d["id"], d["nome"], d["email"], d["fone"])
class ClienteUI:
    objetos = []

    @staticmethod
    def main():
        ClienteUI.abrir()
        while True:
            op = ClienteUI.menu()
            if op == 1: ClienteUI.inserir()
            elif op == 2: ClienteUI.listar()
            elif op == 3: ClienteUI.listar_id()
            elif op == 4: ClienteUI.atualizar()
            elif op == 5: ClienteUI.excluir()
            elif op == 6: ClienteUI.abrir()
            elif op == 7: ClienteUI.salvar()
            elif op == 0: break
        print("Aplicação encerrada.")

    @staticmethod
    def menu():
        print("\n=== MENU CLIENTES ===")
        print("1 - Inserir cliente")
        print("2 - Listar todos")
        print("3 - Listar por ID")
        print("4 - Atualizar cliente")
        print("5 - Excluir cliente")
        print("6 - Abrir arquivo")
        print("7 - Salvar arquivo")
        print("0 - Sair")
        return int(input("Opção: "))

    @staticmethod
    def inserir():
        id = int(input("ID: "))
        nome = input("Nome: ")
        email = input("Email: ")
        fone = input("Fone: ")
        cliente = Cliente(id, nome, email, fone)
        ClienteUI.objetos.append(cliente)
        print("Cliente inserido com sucesso!")

    @staticmethod
    def listar():
        print("\n=== LISTA DE CLIENTES ===")
        for c in ClienteUI.objetos:
            print(c)

    @staticmethod
    def listar_id():
        id = int(input("Informe o ID: "))
        for c in ClienteUI.objetos:
            if c.get_id() == id:
                print(c)
                return
        print("Cliente não encontrado.")

    @staticmethod
    def atualizar():
        id = int(input("Informe o ID para atualizar: "))
        for c in ClienteUI.objetos:
            if c.get_id() == id:
                nome = input("Novo nome: ")
                email = input("Novo email: ")
                fone = input("Novo fone: ")
                c.set_nome(nome)
                c.set_email(email)
                c.set_fone(fone)
                print("Cliente atualizado.")
                return
        print("Cliente não encontrado.")

    @staticmethod
    def excluir():
        id = int(input("Informe o ID para excluir: "))
        for c in ClienteUI.objetos:
            if c.get_id() == id:
                ClienteUI.objetos.remove(c)
                print("Cliente removido.")
                return
        print("Cliente não encontrado.")

    @staticmethod
    def abrir():
        try:
            with open("clientes.json", mode="r", encoding="utf-8") as arquivo:
                clientes_json = json.load(arquivo)
                ClienteUI.objetos = [Cliente.from_dict(obj) for obj in clientes_json]
        except FileNotFoundError:
            ClienteUI.objetos = []

    @staticmethod
    def salvar():
        with open("clientes.json", mode="w", encoding="utf-8") as arquivo:
            lista = [c.to_dict() for c in ClienteUI.objetos]
            json.dump(lista, arquivo, indent=4, ensure_ascii=False)
        print("Clientes salvos no arquivo.")
a = ClienteUI
a.main()