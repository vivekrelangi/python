from functools import reduce


def add(x,y):
    return x+y
a=list(reduce(add, range(1,11)))
print(a)