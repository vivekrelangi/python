f_path = "text_files/viv.txt"

with open(f_path) as f_obj:
    lines = f_obj.readlines()

for line in lines:
    print(line.rstrip())

f_path = "/home/ghostprime/Desktop/jefb.txt"

with open(f_path) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())