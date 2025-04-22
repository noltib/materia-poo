def iniciais(nome):
    partes = nome.strip().split()
    return ''.join([p[0].upper() for p in partes])
nome_completo = input("Digite seu nome completo: ")
print("Suas iniciais são:", iniciais(nome_completo))
