def multiply(a):
    def inner(b): return a * b

    return inner


fn = multiply(5)
print(fn(10))
print(fn(2))
print(fn(0))
input()