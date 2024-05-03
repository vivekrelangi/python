filename = 'siddhartha.txt'

with open(filename) as f_obj:
    contents = f_obj.read()

print(contents)

with open(filename) as f_o:
    for line in f_o:
        print(line.rstrip())