valores = []
for i in range(4):
    num = int(input(f"Digite o {i+1}º valor inteiro: "))
    valores.append(num)

if len(set(valores)) != 4:
    print("Erro: os valores devem ser diferentes entre si.")
else:
    valores_ordenados = sorted(valores)
    menor = valores_ordenados[0]
    segundo_menor = valores_ordenados[1]
    segundo_maior = valores_ordenados[2]
    maior = valores_ordenados[3]

    print("Maior valor =", maior)
    print("Menor valor =", menor)
    print("A soma do segundo maior valor com o segundo menor =", segundo_maior + segundo_menor)