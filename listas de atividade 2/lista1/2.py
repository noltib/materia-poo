valores = []

for i in range(4):
    numero = int(input(f"Digite o {i+1}º valor inteiro: "))
    valores.append(numero)

media = sum(valores) / 4

print(f"Média = {media:.0f}")  # Exibe a média como número inteiro, sem casas decimais

print("Números menores que a média:")
for num in valores:
    if num < media:
        print(num)

print("Números maiores ou iguais à média:")
for num in valores:
    if num >= media:
        print(num)