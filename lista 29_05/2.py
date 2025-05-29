class Frete:
    def __init__(self, distancia, peso):
        if distancia <= 0 or peso <= 0:
            raise ValueError("Distância e peso devem ser positivos.")
        self.__distancia = distancia
        self.__peso = peso

    def set_distancia(self, distancia):
        if distancia > 0:
            self.__distancia = distancia

    def set_peso(self, peso):
        if peso > 0:
            self.__peso = peso

    def get_distancia(self):
        return self.__distancia

    def get_peso(self):
        return self.__peso

    def calc_frete(self):
        return self.__distancia * self.__peso * 0.01

    def __str__(self):
        return f"Frete: distância = {self.__distancia} km, peso = {self.__peso} kg, valor = R${self.calc_frete():.2f}"

print(Frete(15,2))