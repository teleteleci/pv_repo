a = list(range(5))
print(a)


# map
def add_one(x):
    x += 1
    return x


rslt = list(map(add_one, a))
print(rslt)

# the same but with lambda
rslt = list(map(lambda x: x + 1, a))
print(rslt)

# filter -lambda only
rslt = list(filter(lambda x: x >= 2, a))
print(rslt)
