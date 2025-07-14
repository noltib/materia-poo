import random

class Bingo:
    def __init__(self, num_bolas):
        self.__num_bolas = num_bolas
        if num_bolas < 5: raise ValueError("Número mínimo de bolas é 5")
        self.__bolas = []

    def sortear(self):
        if len(self.__bolas) == self.__num_bolas:
            return -1
        x = random.randint(1, self.__num_bolas)
        while x in self.__bolas:
            x = random.randint(1, self.__num_bolas)
        self.__bolas.append(x)
        return x

    def sorteados(self):
        return sorted(self.__bolas)
    
class BingoUI:
    @staticmethod
    def main():
        op = 0
        while op != 4:
            op = BingoUI.menu()
            if op == 1: jogo = BingoUI.iniciar_jogo()
            if op == 2: BingoUI.sortear(jogo)
            if op == 3: BingoUI.sorteados(jogo)

    @staticmethod
    def menu():
        return int(input("1-Iniciar Jogo, 2-Sortear, 3-Sorteados, 4-Fim: "))

    @staticmethod
    def iniciar_jogo():
        jogo = Bingo(int(input("Informe o número de bolas: ")))
        return jogo

    @staticmethod
    def sortear(jogo):
        print(jogo.sortear())

    @staticmethod
    def sorteados(jogo):
        print(jogo.sorteados())

BingoUI.main()

