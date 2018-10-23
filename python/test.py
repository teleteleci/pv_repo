print("test]")


def function(*args):
    for i in args:
        print(i)


function(1, 2, 3)
print("------")

t = [2, 1]
a, b = t
print("[{0}, {1}]".format(a, b))
a, b = b, a
print("[{0}, {1}]".format(a, b))


def f1(**qargs):
    for i in qargs:
        print("{0} = {1}".format(i, qargs[i]))


f1(a=0, b=2)

for i in range(3):
    print(i)
