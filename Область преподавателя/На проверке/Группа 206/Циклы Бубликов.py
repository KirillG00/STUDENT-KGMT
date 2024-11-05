while True:
    s = int(input("Введите первое число: "))
    f = int(input("Введите второе число: "))
    print("Сумма чисел: ", s + f )
    t = input ("Нажмите Y или y для завершения программы: ")
    if (t == "Y" or t == "y"):  break

n = 7
for i in range(0, n):
    for j in range(0, n):
        if(i == 0 or i == n-1 or j==i or j == n-i-1): print("*", end="")
        else: print(" ", end="")
    print()

g = 7
w = g + 2
m = w // 4
for i in range(1, g+1):
    if (i <= m):
        print(" " * (m-i) + "*" * (2*i) + " " * (w-2*i-2*m) + "*" *(2*i) + " " * (m-i))
    else:
        print(" " * (i - 2*m+1) + "*" * (w-2*(i-2*m+1)) + " " * (i - 2*m+1))

gool = 5
goida = 1
counter = 1
for i in range(gool):
    for j in range(gool):
        if goida % 2 == 0:
            print(counter, end="  ")
            counter += 1
        else: print("*", end="  ")
        goida += 1
    print()