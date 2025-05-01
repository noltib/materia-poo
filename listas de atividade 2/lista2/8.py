frase = input("digite sua frase: ").split()
for i in frase:
    b = [letra for letra in i]
    print(b[-1],end=" ")

print("")
