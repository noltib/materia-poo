entrada = input("Digite uma sequência de números separados por vírgula:\n")
numeros = [int(n) for n in entrada.split(',')]
print("Soma =", sum(numeros))
