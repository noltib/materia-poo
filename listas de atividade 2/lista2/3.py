print("resultado:", end=" ")
for i in range(1,11,):
    if i%2 == 0:
        print(f"{i*-1}",end=" ")
    else:
        print(f"{i}",end=" ")
    
print("")