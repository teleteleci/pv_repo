my_list = list(range(5))
print(my_list)
print(list(map(lambda x: x * 2, my_list)))
print((lambda x: x * 2), (for x in my_list))
