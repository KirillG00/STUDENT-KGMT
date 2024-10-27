#циклы 2
n = 7
for i in range(0, n): 
    for j in range(0, n): 
        if(i == 0 or i == n-1 or j==i or j == n-i-1): print("*", end="")
        else: print(" ", end="")
    print()
    
input()