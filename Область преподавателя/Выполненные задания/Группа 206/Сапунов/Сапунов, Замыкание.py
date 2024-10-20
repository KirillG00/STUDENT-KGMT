def multiply(n): return lambda m: n * m


fn = multiply(4)
print(fn(6))
print(fn(9))
print(fn(2))