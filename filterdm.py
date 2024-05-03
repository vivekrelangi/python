def f(x):
    return x%2 !=0 and x%3 != 0
a=list(filter(f,range(2,25)))
print(a)