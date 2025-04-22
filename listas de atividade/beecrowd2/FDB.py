import math
a, b, c = map(float, input().split())
if a != 0:
    delta = b**2-4*a*c
    if delta >= 0:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"R1 = {raiz1:.5f}")
        print(f"R2 = {raiz2:.5f}")

    else:
        print("Impossivel calcular")
else:
    print("Impossivel calcular")