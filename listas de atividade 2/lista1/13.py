entrada = input("Digite dez valores inteiros separados por espaço: ")

numeros = list(map(int, entrada.split()))

if len(numeros) != 10:
    print("Erro: você deve digitar exatamente 10 números.")
else:
    maior = max(numeros)
    menor = min(numeros)
    print(f"O maior valor é {maior} e o menor é {menor}")