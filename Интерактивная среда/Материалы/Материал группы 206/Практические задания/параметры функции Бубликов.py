def sum_range(start, end):
    if start < end:
        return sum(range(start, end + 1))
    else:
        return sum(range(end, start + 1))


g = int(input())
h = int(input())

print(sum_range(g, h))

input()