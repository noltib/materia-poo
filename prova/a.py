class Viagem:
    def __init__(self):
        self.__destino = ""
        self.__distancia = 0.0
        self.__litros = 0.0

    def set_destino(self, dest):
        if isinstance(dest, str):
            self.__destino = dest
        else:
            raise ValueError("O destino deve ser uma string.")

    def get_destino(self):
        return self.__destino

    def set_distancia(self, dist):
        if dist > 0:
            self.__distancia = dist
        else:
            raise ValueError("A distância deve ser maior que zero.")

    def get_distancia(self):
        return self.__distancia

    def set_litros(self, lit):
        if lit > 0:
            self.__litros = lit
        else:
            raise ValueError("Os litros devem ser maiores que zero.")

    def get_litros(self):
        return self.__litros

    def consumo(self):
        return self.__distancia / self.__litros

    def __str__(self):
        return (f"Destino: {self.__destino}\n"
                f"Distância: {self.__distancia} km\n"
                f"Combustível: {self.__litros} L\n"
                f"Consumo médio: {self.consumo():.2f} km/L")


class ViagemUI:
    def menu(self):
        print("\n1 - Calcular Consumo")
        print("2 - Fim")
        return input("Escolha uma opção: ")

    def main(self):
        while True:
            opcao = self.menu()
            if opcao == "1":
                self.calculo()
            elif opcao == "2":
                print("Encerrando...")
                break
            else:
                print("Opção inválida.")

    def calculo(self):
        viagem = Viagem()
        viagem.set_destino(input("Informe o destino: "))
        try:
            distancia = float(input("Informe a distância (km): "))
            viagem.set_distancia(distancia)
            litros = float(input("Informe os litros gastos: "))
            viagem.set_litros(litros)

            print("\nResultado:")
            print(viagem)  # Usando __str__()

        except ValueError:
            print("Erro: informe apenas números válidos.")
