                                #списки ЗАДАНИЕ 3
mat = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

for i in range(3):
    for j in range(3):
        print(mat[i][j], end = " ")
    print()

                                #списки ЗАДАНИЕ 4

list1 = [10, 20, 10, 20, 30, 40, 30, 50]
list2 = []
for n in list1:
    if n not in list2:
        list2.append(n)
print(list1)
print(list2)

input()