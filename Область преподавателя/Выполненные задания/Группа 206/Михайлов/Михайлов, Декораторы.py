def check(input_func):
    def output_func(*args):
        result = input_func(*args)
        if result < 0: result = 0
        return result
    return output_func
def sum(a, b):
    return a + b
result1 = sum(15, 20)
print(result1)
result2 = sum(15, -20)
print(result2)

input()