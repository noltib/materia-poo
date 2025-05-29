import math

class Retangulo:
    def __init__(self, base, altura):
        if base <= 0 or altura <= 0:
            raise ValueError("Base e altura devem ser positivas.")
        self.__base = base
        self.__altura = altura

    def set_base(self, base):
        if base > 0:
            self.__base = base

    def set_altura(self, altura):
        if altura > 0:
            self.__altura = altura

    def get_base(self):
        return self.__base

    def get_altura(self):
        return self.__altura

    def calc_area(self):
        return self.__base * self.__altura

    def calc_diagonal(self):
        return math.sqrt(self.__base**2 + self.__altura**2)

    def __str__(self):
        return f"Retângulo: base = {self.__base}, altura = {self.__altura}, área = {self.calc_area():.2f}, diagonal = {self.calc_diagonal():.2f}"
print(Retangulo(2,3))