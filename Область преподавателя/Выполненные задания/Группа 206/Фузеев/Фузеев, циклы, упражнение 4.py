n=5
k=1
counter=1
for i in range(n):
    for j in range(n):
        if k % 2 == 0:
            print(counter, end ="  ")
            counter+=1
        else: print("*",end="  ")
        k+=1
    print()
input()