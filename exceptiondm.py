try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide a number by zero")
    
f_n = 'sam.txt'

try:
    with open(f_n) as f:
        lines = f.readlines()
except FileNotFoundError:
    msg = "Can't find file {0}.".format(f_n)
    print(msg)