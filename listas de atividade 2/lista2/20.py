for i in range(1, 11):
    linha = [str(i)]
    pares = [str(n) for n in range(2, i + 1, 2)]
    linha.extend(pares)
    print(' '.join(linha))
