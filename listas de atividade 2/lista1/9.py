entrada = input("Digite o horário no formato hh:mm: ")

try:
    hora, minuto = map(int, entrada.split(":"))

    if not (0 <= hora <= 23 and 0 <= minuto < 60):
        print("Hora Inválida")
    else:
        hora %= 12

        ang_hora = 30 * hora + 0.5 * minuto
        ang_minuto = 6 * minuto
        angulo = abs(ang_hora - ang_minuto)

        if angulo > 180:
            angulo = 360 - angulo

        print(f"Menor ângulo entre os ponteiros = {int(angulo)} graus")
except:
    print("Hora Inválida")