from datetime import datetime

class EntradaCinema:
    def __init__(self, dia, horario):
        self.dia = dia
        self.horario = datetime.strptime(horario, "%H:%M")

    def calcular_valor_entrada(self):
        valor_base = 0
        if self.dia in ["segunda", "terca", "quinta"]:
            valor_base = 16
        elif self.dia == "quarta":
            return 8
        elif self.dia in ["sexta", "sabado", "domingo"]:
            valor_base = 20

        if 17 <= self.horario.hour < 24:
            valor_base *= 1.5

        return valor_base

dia = input("Digite o dia da semana: ").lower()
horario = input("Digite o horário da sessão (HH:MM): ")

entrada = EntradaCinema(dia, horario)
print(f"Valor da entrada: R$ {entrada.calcular_valor_entrada():.2f}")
