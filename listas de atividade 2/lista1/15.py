valores = []
for i in range(3):
    numero = int(input(f"Digite o {i+1}º valor: "))
    valores.append(numero)

valores.sort()

print(f"{valores[0]}, {valores[1]}, {valores[2]}")