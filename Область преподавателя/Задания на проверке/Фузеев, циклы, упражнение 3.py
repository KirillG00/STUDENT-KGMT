h = 7
w = h + 2
m = w //4
for i in range(1, h+1):
    if (i <= m):
        print(" " * (m-i) + "*" * (2*i) + " " * (w-2*i-2*m) + "*" *(2*i) + " " * (m-i))
    else:
      print(" " * (i - 2*m+1) + "*" * (w-2*(i-2*m+1)) + " " * (i - 2*m+1))
      
input()