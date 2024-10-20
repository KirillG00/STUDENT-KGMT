def multiply(a): return lambda m: a * m


fn = multiply(5)
print(fn(5))  # 25
print(fn(6))  # 30
print(fn(7))  # 35