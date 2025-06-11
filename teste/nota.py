b = int(input())
t = int(input())
calculo = (b+t)*70/2
calculo2 = (160-b + 160-t)*70/2
if calculo == calculo2:
    print("0")
elif calculo > calculo2:
    print("1")
elif calculo < calculo2:
    print("2")
