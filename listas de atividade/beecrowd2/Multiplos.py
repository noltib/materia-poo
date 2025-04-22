a, b = map(int, input().split())
maior = max(a,b)
menor = min(a,b)
if maior % menor == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")