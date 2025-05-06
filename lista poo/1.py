import math
class Circulo:
    def __init__(self, raio):
        self.raio = raio
    def calcular_area(self):
        return math.pi * (self.raio ** 2)
    def calcular_circunferencia(self):
        return 2 * math.pi * self.raio
raio = float(input("Digite o raio do círculo: "))
circulo = Circulo(raio)
print(f"Área do círculo: {circulo.calcular_area():.2f}")
print(f"Circunferência do círculo: {circulo.calcular_circunferencia():.2f}")
