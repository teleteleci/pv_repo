# is used for generating data
#
# instead of list has no memmory restriction


def generator():
    for i in range(5):
        yield i


print(list(generator()))
