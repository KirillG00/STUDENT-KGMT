a = 7
b = a + 2
c = b //4
for i in range(1, a+1):
    if (i <= c):
        print(" " * (c-i) + "*" * (2*i) + " " * (b-2*i-2*c) + "*" *(2*i) + " " * (c-i))
    else:
      print(" " * (i - 2*c+1) + "*" * (b-2*(i-2*c+1)) + " " * (i - 2*c+1))
      
input()