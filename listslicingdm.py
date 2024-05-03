finishers=['kai','abe','ada','gus','zoe']
first_three=finishers[:3]
s=int(len(finishers)/2-1)
e=int(len(finishers)/2+2)
middle_three=finishers[s:e]
last_three=finishers[-3:]
print(first_three,last_three,middle_three,s,e)
#opy a list
copy_of_finishers=finishers[:]
print(copy_of_finishers)