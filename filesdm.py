filename = 'siddhartha.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line,end=" ")
filename = 'journal.txt'
with open(filename,'w') as file_object:
    #n=int(input("Enter the number of lines you wanna write:"))
    line=""
    while line!="exi1t":
        line=input("Enter line:")
        if line!="exi1t":
            file_object.write(line)
            file_object.write("\n")
        """if line == "exi1t":
            file_object."""
filename='journal1.txt'
with open(filename,'a') as file_object:
    file_object.write("\nI love making games.")