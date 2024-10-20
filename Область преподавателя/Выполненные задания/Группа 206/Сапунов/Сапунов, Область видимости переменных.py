def outer():
    n = 7

    def inner():
        n = 34
        print(n)

    inner()
    print(n)


outer()