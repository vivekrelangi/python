filename = 'siddhartha.txt'
 
with open(filename) as f_o:
    lines = f_o.readlines()

for line in lines:
    print(line.rstrip())

print(lines)
