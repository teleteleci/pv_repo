# is used for change function behavior


# now I define some decor function
def decor(func):
    def wrap():
        print("--------------------------------------")
        func()
        print("--------------------------------------")
    return wrap()


# origin function
def origin_fce():
    print("hello word")


decorated = decor(origin_fce)
decorated()
