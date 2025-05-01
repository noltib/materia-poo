print("resultado:", end=" ")
for i in range(1,31):
    if i%3 == 0:
        print(f"{i*-1}",end=" ")
    else:
        print(f"{i}",end=" ")
    
print("")