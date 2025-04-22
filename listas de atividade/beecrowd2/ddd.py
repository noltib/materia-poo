ddds = {
    61: "Brasilia",
    71: "Salvador",
    11: "Sao Paulo",
    21: "Rio de Janeiro",
    32: "Juiz de Fora",
    19: "Campinas",
    27: "Vitoria",
    31: "Belo Horizonte"
}
codigo_ddd = int(input())
if codigo_ddd in ddds:
    print(ddds[codigo_ddd])
else:
    print("DDD nao cadastrado")
