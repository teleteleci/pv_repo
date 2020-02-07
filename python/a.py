# def a(name='x'):
#     print('--- {} ---'.format(name))
#
#
# def a_decorator(func):
#     print('----------')
#     func()
#     print('----------')
#
#
# if __name__ == '__main__':
#     # a()
#     a_decorator(a)

a = 'xxxxabcdbbdk'
t = {}


def readDict(text: str) -> dict:
    t = {}
    for l in text:
        try:
            t[l] = t[l] + l
        except KeyError:
            t[l] = l
    return t


def beautify(d: dict) -> str:
    c = ''
    for i in sorted(d):
        # print(d[i])
        c += '_' + d[i]

    return(c[1:])


print(a)
r = beautify(readDict(a))
print(r)
print(r[::-1])

t = 'dcbbbba'
x = tuple(t)
print(x[-1:])
print(x[:-1])
print(x[::-1])
print(x[1:])
print(x[:1])
print(sorted(x))
print(set(x))
print(x.count('b'))
print('t' in x)
