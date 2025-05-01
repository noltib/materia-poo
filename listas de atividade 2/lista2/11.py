frase = input("Digite uma frase: ")
soma = 0
for caractere in frase:
    if caractere.isdigit():
        soma += int(caractere)
print(soma)