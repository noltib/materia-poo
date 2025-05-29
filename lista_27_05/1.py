import math

class Circulo:
    def __init__(self, raio):
        self.__raio = raio

    def set_raio(self, raio):
        self.__raio = raio

    def get_raio(self):
        return self.__raio

    def calcular_area(self):
        return math.pi * self.__raio ** 2

    def calcular_circunferencia(self):
        return 2 * math.pi * self.__raio

c = Circulo(5)
print("Raio:", c.get_raio())
print("Área:", c.calcular_area())
print("Circunferência:", c.calcular_circunferencia())
