def sum_range(start, end):
    if start < end:
        return sum(range(start, end + 1))
    else:
        return sum(range(end, start + 1))


s = int(input())
e = int(input())

print(sum_range(s, e))

input()