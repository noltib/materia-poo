maior_valor = -1
posicao = -1
for i in range(1, 101):
    valor = int(input())
    if valor > maior_valor:
        maior_valor = valor
        posicao = i
print(maior_valor)
print(posicao)
