# types
# tuple imutable ordered sequence of value
tuple_a = (1, 2, 3, 4)
# mutable key value array
dictionary_a = {"a": 1, "b": "xxx"}
list_a = [1, 2, 3]
set_a = {1, 2, 3, 1}  # Unique array ignore duplicity {1, 2, 3}
set_b = {2, 3, 4}

# Tuple can not be changed
try:
    tuple_a[1] = -2
except TypeError:
    print("tuple can not be changed")


# playing with sets
# join
print(set_a | set_b)
# intersection
print(set_a & set_b)
# diference a - b
print(set_a - set_b)
# diference b - a
print(set_b - set_a)
# symetric difference
print(set_a ^ set_b)

# zip function
print(dict(zip("abcd", "0123")))
