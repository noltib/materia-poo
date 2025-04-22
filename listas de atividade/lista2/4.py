frase = input("Digite uma frase: ")
ultimo_espaco = frase.rfind(' ')
ultima_palavra = frase[ultimo_espaco + 1:]
print(ultima_palavra)