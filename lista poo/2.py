class Viagem:
    def __init__(self, distancia, horas, minutos):
        self.distancia = distancia
        self.horas = horas
        self.minutos = minutos

    def calcular_velocidade_media(self):
        tempo_em_horas = self.horas + self.minutos / 60
        return self.distancia / tempo_em_horas

distancia = float(input("Digite a distância da viagem em km: "))
horas = int(input("Digite o tempo gasto em horas: "))
minutos = int(input("Digite o tempo gasto em minutos: "))

viagem = Viagem(distancia, horas, minutos)
print(f"Velocidade média da viagem: {viagem.calcular_velocidade_media():.2f} km/h")
