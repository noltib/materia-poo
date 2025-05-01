frase = input("digite sua frase: ").split()
a = len(frase)
for i in range(a):
    for b in frase:
        print(b,end=" ")
    print("")
    frase.pop(0)