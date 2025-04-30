import datetime
def data_valida(dia, mes, ano):
    try:
        datetime.datetime(ano, mes, dia)
        return True
    except ValueError:
        return False

data = input("Digite uma data no formato dd/mm/aaaa: ")

try:
    dia, mes, ano = map(int, data.split("/"))

    if 1900 <= ano <= 2100 and 1 <= mes <= 12 and data_valida(dia, mes, ano):
        print("A data informada é válida")
    else:
        print("A data informada não é válida")
except ValueError:
    print("A data informada não é válida")
