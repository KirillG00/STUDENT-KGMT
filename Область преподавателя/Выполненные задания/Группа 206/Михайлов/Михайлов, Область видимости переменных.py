def outer():
    p = 3
    def inner():
        nonlocal p
        p = 9
        print(p)
    inner()
    print(p)
outer()

input()