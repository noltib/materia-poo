meses = [
    "janeiro", "fevereiro", "março",
    "abril", "maio", "junho",
    "julho", "agosto", "setembro",
    "outubro", "novembro", "dezembro"
]

numero = int(input("Informe o número do mês (1 a 12): "))

if 1 <= numero <= 12:
    nome_mes = meses[numero - 1]

    if numero <= 3:
        trimestre = "primeiro"
    elif numero <= 6:
        trimestre = "segundo"
    elif numero <= 9:
        trimestre = "terceiro"
    else:
        trimestre = "quarto"

    print(f"O mês de {nome_mes} é do {trimestre} trimestre do ano.")
else:
    print("Número de mês inválido.")