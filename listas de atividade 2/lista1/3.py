pares = 0
impares = 0

for i in range(4):
    numero = int(input(f"Digite o {i+1}º valor inteiro: "))
    if numero % 2 == 0:
        pares += numero
    else:
        impares += numero

print("Soma dos pares =", pares)
print("Soma dos ímpares =", impares)