frase = input("Digite uma frase:\n")
palavras = frase.split()
senha = ''.join(str(len(palavra)) for palavra in palavras)
print(senha)
