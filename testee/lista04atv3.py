class Pais:
    def __init__(self, i: int, n: str, p: int, a: float):
        self.__id = i
        self.__nome = n
        self.__populacao = p
        self.__area = a

    def Densidade(self) -> float:
        if self.__area > 0:
            return self.__populacao / self.__area
        else:
            return 0.0

    def ToString(self) -> str:
        return f"ID: {self.__id}, Nome: {self.__nome}, População: {self.__populacao}, Área: {self.__area:.2f}, Densidade: {self.Densidade():.2f}"

    def get_id(self) -> int:
        return self.__id

    def get_nome(self) -> str:
        return self.__nome

    def get_populacao(self) -> int:
        return self.__populacao

    def get_area(self) -> float:
        return self.__area

    def set_dados(self, n: str, p: int, a: float):
        self.__nome = n
        self.__populacao = p
        self.__area = a

class PaisUI:
    __paises = []

    @staticmethod
    def Main():
        while True:
            op = PaisUI.Menu()
            if op == 1:
                PaisUI.Inserir()
            elif op == 2:
                PaisUI.Listar()
            elif op == 3:
                PaisUI.Atualizar()
            elif op == 4:
                PaisUI.Excluir()
            elif op == 5:
                PaisUI.MaisPopuloso()
            elif op == 6:
                PaisUI.MaisPovoado()
            elif op == 7:
                print("Encerrando...")
                break
            else:
                print("Opção inválida!")

    @staticmethod
    def Menu() -> int:
        print("=== MENU DE PAÍSES ===")
        print("1 - Inserir país")
        print("2 - Listar países")
        print("3 - Atualizar país")
        print("4 - Excluir país")
        print("5 - Mostrar país mais populoso")
        print("6 - Mostrar país mais povoado")
        print("7 - Sair")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return 0

    @staticmethod
    def Inserir():
        try:
            i = int(input("ID: "))
            n = input("Nome: ")
            p = int(input("População: "))
            a = float(input("Área: "))
            novo = Pais(i, n, p, a)
            PaisUI.__paises.append(novo)
            print("País inserido com sucesso!")
        except ValueError:
            print("Dados inválidos.")

    @staticmethod
    def Listar():
        if PaisUI.__paises:
            print("Lista de Países:")
            for p in PaisUI.__paises:
                print(p.ToString())
        else:
            print("Nenhum país cadastrado.")

    @staticmethod
    def Atualizar():
        try:
            idBusca = int(input("Digite o ID do país a ser atualizado: "))
            for p in PaisUI.__paises:
                if p.get_id() == idBusca:
                    n = input("Novo nome: ")
                    pop = int(input("Nova população: "))
                    area = float(input("Nova área: "))
                    p.set_dados(n, pop, area)
                    print("Dados atualizados.")
                    return
            print("País não encontrado.")
        except ValueError:
            print("Entrada inválida.")

    @staticmethod
    def Excluir():
        try:
            idBusca = int(input("Digite o ID do país a excluir: "))
            for i, p in enumerate(PaisUI.__paises):
                if p.get_id() == idBusca:
                    PaisUI.__paises.pop(i)
                    print("País removido.")
                    return
            print("País não encontrado.")
        except ValueError:
            print("Entrada inválida.")

    @staticmethod
    def MaisPopuloso():
        if not PaisUI.__paises:
            print("Nenhum país cadastrado.")
            return
        mais = max(PaisUI.__paises, key=lambda p: p.get_populacao())
        print("País mais populoso:")
        print(mais.ToString())

    @staticmethod
    def MaisPovoado():
        if not PaisUI.__paises:
            print("Nenhum país cadastrado.")
            return
        mais = max(PaisUI.__paises, key=lambda p: p.Densidade())
        print("País mais povoado:")
        print(mais.ToString())
PaisUI.Main()