import math
base = int(input("digite sua base "))
altura = int(input("digite sua altura "))
area = base*altura
perimetro = 2*(base + altura)
diagonal = math.sqrt(base**2 + altura**2)
print(f"area: {area:.2f}   perimetro: {perimetro:.2f}    diagonal: {diagonal:.2f}")