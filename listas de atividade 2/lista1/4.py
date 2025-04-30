def horario_para_minutos(horario):
    horas, minutos = map(int, horario.split(":"))
    return horas * 60 + minutos

def minutos_para_horario(total_minutos):
    horas = total_minutos // 60
    minutos = total_minutos % 60
    return f"{horas:02d}:{minutos:02d}"

h1 = input("Digite o primeiro horário no formato hh:mm: ")
h2 = input("Digite o segundo horário no formato hh:mm: ")

total_minutos = horario_para_minutos(h1) + horario_para_minutos(h2)

horario_total = minutos_para_horario(total_minutos)
print("Total de horas =", horario_total)