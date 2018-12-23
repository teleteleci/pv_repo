import numpy as np
from timeit import timeit

# setup = 'from __main__ import count_transitions, x; import numpy as np'
# num = 1000
#
# t1 = timeit('count_transitions(x)', setup=setup, number=num)
# t2 = timeit('np.count_nonzero(x[:-1] < x[1:])', setup=setup, number=num)
#
# print('Speed difference: {:0.1f}x'.format(t1 / t2))

t1 = timeit(stmt="a.append(1)", setup='a=[]', number=10000000)
print(t1)
# t2 = timeit(stmt="", setup="")
a = np.array(10000000)
print(a)
