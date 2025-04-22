def formatar_nome(nome):
    return ' '.join([parte.capitalize() for parte in nome.strip().split()])
nome = input("Digite seu nome: ")
print("Nome formatado:", formatar_nome(nome))
