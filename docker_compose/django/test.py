def fib(n):
    rslt = []
    a, b = 0, 1
    while a < n:
        rslt.append(a)
        a, b = b, a + b

    return rslt


if __name__ == '__main__':
    print(dir())
    print(fib(500))
