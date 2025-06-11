class Pessoa:
    def __init__(self, nome, peso, altura):
        self.set_nome(nome)
        self.set_peso(peso)
        self.set_altura(altura)

    def get_nome(self):
        return self.__nome

    def get_peso(self):
        return self.__peso

    def get_altura(self):
        return self.__altura

    def set_nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise ValueError("nome precisa ser string")

    def set_peso(self, peso):
        if isinstance(peso, float) and peso > 0:
            self.__peso = peso
        else:
            raise ValueError("peso precisa ser float positivo")

    def set_altura(self, altura):
        if isinstance(altura, float) and altura > 0:
            self.__altura = altura
        else:
            raise ValueError("altura precisa ser float positivo")

    def calcular_imc(self):
        return self.__peso / (self.__altura ** 2)


class PessoaUI:
    def menu(self):
        print("MENU")
        print("1 - Calcular IMC")
        print("2 - Sair")
        opcao = int(input("Escolha uma opção: "))
        return opcao

    def calculo(self):
        try:
            nome = input("Digite o nome: ")
            peso = float(input("Digite o peso (kg): "))
            altura = float(input("Digite a altura (m): "))

            pessoa = Pessoa(nome, peso, altura)

            print("=== Resultado ===")
            print(f"Nome: {pessoa.get_nome()}")
            print(f"Peso: {pessoa.get_peso()} kg")
            print(f"Altura: {pessoa.get_altura()} m")
            print(f"IMC: {pessoa.calcular_imc():.2f}")
        except ValueError as e:
            print(f"Erro: {e}")

    def main(self):
        while True:
            opcao = self.menu()
            if opcao == 1:
                self.calculo()
            elif opcao == 2:
                print("Saindo...")
                break
            else:
                print("Opção inválida, tente novamente")


ui = PessoaUI()
ui.main()
