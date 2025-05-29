class EntradaCinema:
    def __init__(self, dia, hora):
        self.__dia = dia.lower()
        self.__hora = hora

    def set_dia(self, dia):
        self.__dia = dia.lower()

    def set_hora(self, hora):
        self.__hora = hora

    def get_dia(self):
        return self.__dia

    def get_hora(self):
        return self.__hora

    def calcular_valor(self):
        if self.__dia == "quarta":
            return 8.00, 8.00

        if self.__dia in ["segunda", "terça", "quinta"]:
            valor_base = 16.00
        elif self.__dia in ["sexta", "sábado", "domingo"]:
            valor_base = 20.00
        else:
            valor_base = 0.00

        if 17 <= self.__hora <= 23:
            valor_base *= 1.5

        return valor_base, valor_base / 2

entrada = EntradaCinema("sexta", 18)
inteira, meia = entrada.calcular_valor()
print("Dia:", entrada.get_dia())
print("Hora:", entrada.get_hora())
print("Valor inteira: R$", inteira)
print("Valor meia: R$", meia)
