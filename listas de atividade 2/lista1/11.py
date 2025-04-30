meses = [
    "janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
]

data = input("Digite uma data no formato dd/mm/aaaa: ")

try:
    dia, mes, ano = map(int, data.split("/"))

    if 1 <= mes <= 12:
        print(f"A data é {dia} de {meses[mes - 1]} de {ano}")
    else:
        print("A data informada não é válida")
except ValueError:
    print("A data informada não é válida")