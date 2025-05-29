import math

class Equacao2Grau:
    def __init__(self, a, b, c):
        if a == 0:
            raise ValueError("O coeficiente 'a' deve ser diferente de zero.")
        self.__a = a
        self.__b = b
        self.__c = c

    def set_coeficientes(self, a, b, c):
        if a != 0:
            self.__a = a
            self.__b = b
            self.__c = c

    def get_coeficientes(self):
        return self.__a, self.__b, self.__c

    def delta(self):
        return self.__b**2 - 4 * self.__a * self.__c

    def tem_raizes_reais(self):
        return self.delta() >= 0

    def raiz1(self):
        d = self.delta()
        if d < 0:
            return None
        return (-self.__b + math.sqrt(d)) / (2 * self.__a)

    def raiz2(self):
        d = self.delta()
        if d < 0:
            return None
        return (-self.__b - math.sqrt(d)) / (2 * self.__a)

    def __str__(self):
        return (f"Equação: {self.__a}x² + {self.__b}x + {self.__c} = 0\n"
                f"Delta = {self.delta():.2f}, "
                f"Raízes reais: {'Sim' if self.tem_raizes_reais() else 'Não'}, "
                f"Raiz1 = {self.raiz1()}, Raiz2 = {self.raiz2()}")

print(Equacao2Grau(3,4,5))