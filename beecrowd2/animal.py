a = input().strip()  # vertebrado ou invertebrado
b = input().strip()  # mamifero, ave, anelideo, etc.
c = input().strip()  # onivoro, carnivoro, herbivoro, etc.

# Lógica de decisão
if a == "vertebrado":
    if b == "mamifero":
        if c == "onivoro":
            print("homem")
        elif c == "herbivoro":
            print("vaca")
    elif b == "ave":
        if c == "carnivoro":
            print("aguia")
        elif c == "onivoro":
            print("pomba")
elif a == "invertebrado":
    if b == "anelideo":
        if c == "onivoro":
            print("minhoca")
        elif c == "hematofago":
            print("sanguessuga")
    elif b == "inseto":
        if c == "hematofago":
            print("pulga")
        elif c == "herbivoro":
            print("lagarta")