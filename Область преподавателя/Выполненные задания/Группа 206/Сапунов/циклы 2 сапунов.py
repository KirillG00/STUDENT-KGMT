p = 7
for i in range(0, p):
    for j in range(0, p):
        if(i ==  0 or i == p - 1 or j == i or j == p - i - 1): print('*', end="")
        else: print(" ", end="")
    print()
    
input()