class Viagem:
    def __init__(self, distancia, horas, minutos):
        self.__distancia = distancia
        self.__horas = horas
        self.__minutos = minutos

    def set_distancia(self, distancia):
        self.__distancia = distancia

    def set_tempo(self, horas, minutos):
        self.__horas = horas
        self.__minutos = minutos

    def get_distancia(self):
        return self.__distancia

    def get_tempo(self):
        return (self.__horas, self.__minutos)

    def calcular_velocidade_media(self):
        tempo_horas = self.__horas + self.__minutos / 60
        return self.__distancia / tempo_horas if tempo_horas > 0 else 0

v = Viagem(120, 2, 30)
print("Distância:", v.get_distancia(), "km")
print("Tempo:", v.get_tempo(), "h")
print("Velocidade média:", v.calcular_velocidade_media(), "km/h")
