def multiply(p): return lambda m: p * m
fp = multiply(5)
print(fp(5))
print(fp(6))
print(fp(7))

input()