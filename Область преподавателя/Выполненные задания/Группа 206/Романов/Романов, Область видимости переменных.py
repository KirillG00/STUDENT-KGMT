def outer():
    a = 5

    def inner():
        nonlocal a
        a = 25
        print(a)

    inner()
    print(a)


outer()