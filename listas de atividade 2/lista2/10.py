frase = input("Digite uma frase: ")
original = frase

while True:
    frase = frase[1:] + frase[0]
    print(frase)
    if frase == original:
        break