frase = input("Digite uma frase:\n").lower()
palavras = frase.split()

def contar_vogais(palavra):
    return sum(1 for letra in palavra if letra in "aeiou")

resultado = []
for palavra in palavras:
    repeticoes = contar_vogais(palavra)
    resultado.extend([palavra] * repeticoes)

print(' '.join(resultado))
