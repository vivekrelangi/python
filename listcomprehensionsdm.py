squares=[]
for inc in range(1,11):
    square=inc**2
    squares.append(square)

print(squares)

squares=[x**2 for x in range(1,6)]
print(squares)

names= ['kai','abe','ada','gus','zoe']
upper_names=[name.upper() for name in names]
print(upper_names)