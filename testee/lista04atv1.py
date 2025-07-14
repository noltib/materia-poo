import random

class Bingo:
    def __init__(self, numBolas: int):
        self.__numBolas = numBolas
        self.__bolas = []  
        self.__todasBolas = list(range(1, numBolas + 1))  

    def Sortear(self) -> int:
        if not self.__todasBolas:
            return -1 
        bola = random.choice(self.__todasBolas)
        self.__todasBolas.remove(bola)
        self.__bolas.append(bola)
        return bola

    def Sorteados(self) -> list[int]:
        return self.__bolas.copy()


class BingoUI:
    @staticmethod
    def Main():
        bingo = None
        while True:
            opcao = BingoUI.Menu()
            if opcao == 1:
                bingo = BingoUI.IniciarJogo()
            elif opcao == 2:
                if bingo:
                    BingoUI.Sortear(bingo)
                else:
                    print("Inicie o jogo primeiro!")
            elif opcao == 3:
                if bingo:
                    BingoUI.Sorteados(bingo)
                else:
                    print("Inicie o jogo primeiro!")
            elif opcao == 4:
                print("Encerrando o jogo. Até mais!")
                break
            else:
                print("Opção inválida. Tente novamente.")

    @staticmethod
    def Menu() -> int:
        print("=== MENU DO BINGO ===")
        print("1 - Iniciar novo jogo")
        print("2 - Sortear número")
        print("3 - Ver números sorteados")
        print("4 - Sair")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return 0

    @staticmethod
    def IniciarJogo() -> Bingo:
        while True:
            try:
                n = int(input("Digite o número total de bolas: "))
                if n > 0:
                    print("Novo jogo iniciado com", n, "bolas.")
                    return Bingo(n)
                else:
                    print("O número deve ser maior que zero.")
            except ValueError:
                print("Digite um número válido.")

    @staticmethod
    def Sortear(b: Bingo):
        bola = b.Sortear()
        if bola == -1:
            print("Todas as bolas já foram sorteadas!")
        else:
            print(f"Bola sorteada: {bola}")

    @staticmethod
    def Sorteados(b: Bingo):
        bolas = b.Sorteados()
        if bolas:
            print("Números sorteados até agora:", bolas)
        else:
            print("Nenhuma bola foi sorteada ainda.")



BingoUI.Main()
