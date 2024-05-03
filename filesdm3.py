"""filename = 'programming.txt'

with open(filename, 'w') as f:
    f.write("I love programming!")
"""
filename = 'programming.txt'

with open(filename,'w') as f:
    f.write("I love programming!\n")
    f.write("I love creating new games.\n")

filename = 'programming.txt'

with open(filename, 'a') as f:
    f.write("I also love working with data.\n")
    f.write("I love making apps as well.\n")
