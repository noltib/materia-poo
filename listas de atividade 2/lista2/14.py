frase = input("Digite uma frase:\n")
palavras = frase.split()
for palavra in palavras:
    print(palavra[::-1])
