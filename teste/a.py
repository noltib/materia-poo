class Agua:
    def __init__(self):    # Encapsulamento
        self.__mes = 1
        self.__ano = 2025
        self.__consumo = 0
    def set_mes(self, v):  # método de acesso: set para ajustar o valor do atributo
        if v < 1 or v > 12: raise ValueError("O mês deve estar entre 1 e 12")   # validação
        self.__mes = v  
    def set_ano(self, v):
        if v == 0: raise ValueError("O ano não pode ser zero")                  # validação
        self.__ano = v
    def set_consumo(self, v):
        if v < 0: raise ValueError("O consumo não pode ser negativo")           # validação
        self.__consumo = v   
    def get_mes(self):     # método de acesso: get para retornar o valor do atributo
        return self.__mes           
    def get_ano(self):
        return self.__ano           
    def get_consumo(self):
        return self.__consumo           
    def valor(self):
        if self.__consumo <= 10: return 38
        if 11 <= self.__consumo <= 20: return 38 + (self.__consumo - 10) * 5
        if self.__consumo > 20: return 38 + 50 + (self.__consumo - 20) * 6  

class Triangulo:
    def __init__(self):
        self.__b = 0
        self.__h = 0

    def set_base(self, v):
        if v <= 0:
            raise ValueError("A base deve ser maior que zero.")
        self.__b = v

    def set_altura(self, v):
        if v <= 0:
            raise ValueError("A altura deve ser maior que zero.")
        self.__h = v

    def get_base(self):
        return self.__b

    def get_altura(self):
        return self.__h

    def calc_area(self):
        return self.__b * self.__h / 2


class UI: # UI = User Interface: print e input
    @staticmethod
    def menu():
        op = int(input("Informe uma opção: 1-Conta d'água, 2-Triângulo, 9-Fim: "))
        return op
    @staticmethod
    def main():
        op = 0
        while op != 9:
           # op = self.menu()
           op = UI.menu()
           if op == 1: UI.agua()
           if op == 2: UI.triangulo()
    @staticmethod
    def agua():
        x = Agua() # x é um objeto da classe Água

        # x.mes = int(input("Informe o mês da conta: "))
        x.set_mes(int(input("Informe o mês da conta: ")))

        # x.ano = int(input("informe o ano: "))
        x.set_ano(int(input("informe o ano: ")))

        # x.consumo = int(input("informe o consumo em m3: "))
        x.set_consumo(int(input("informe o consumo em m3: ")))
        
        #print(x.__mes, x.__ano, x.__consumo)
        # __mes, __ano e __consumo não são visíveis

        #print(f"O valor da conta de água do mês {x.mes} do ano {x.ano} é {x.valor()}")
        print(f"O valor da conta de água do mês {x.get_mes()} do ano {x.get_ano()} é {x.valor()}")
    @staticmethod
    def triangulo():
        x = Triangulo() # x é um objeto da classe Triangulo
        x.b = int(input("Informe o valor da base: "))
        x.h = int(input("Informe o valor da altura: "))
        print(f"O triângulo de base {x.b} e altura {x.h} tem área {x.calc_area()}")

#x = UI()
#x.main()
UI.main()