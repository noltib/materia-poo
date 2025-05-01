print("resultado:", end=" ")
for i in range(1,31):
    print(f"{i}",end=" ")
    if i%3 == 0:
        print(i*3-3, end=" ")

print("")