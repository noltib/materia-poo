frase = input("Digite uma frase:\n").lower()
vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for letra in frase:
    if letra in vogais:
        vogais[letra] += 1

for v in 'aeiou':
    print(f"{v.upper()} – {vogais[v]}")