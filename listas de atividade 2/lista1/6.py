valores = []
for i in range(3):
    numero = int(input(f"Digite o {i+1}º valor inteiro: "))
    valores.append(numero)

# Cálculo
maior = max(valores)
menor = min(valores)
soma = maior + menor

# Saída
print(f"A soma do maior com o menor número é {soma}.")