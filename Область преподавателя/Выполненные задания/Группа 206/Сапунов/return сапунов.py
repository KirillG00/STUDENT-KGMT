def sum_range(start, end):
    result = 0
    if start > end:
        start, end = end, start
    for i in range(start, end +1):
        result += i
    return print(result)

start = int(input())
end = int(input())

sum_range(start, end)

input()