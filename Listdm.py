A=[1,"This is a list",1.78,'d',("king","kong")]
inc=0
L=[1,3,4,5]
A.append("yo")
A.extend(L)
A.insert(0,"0")
A.remove('d')
for inc in range(len(A)):
	print(A[inc],end=" ")
	inc+=1
a=[8,1,1,2,3,4,7]
print(a.count(1),a.count(2),a.count('x'))
print(a.index(1))
#print(a)
print(a.reverse())
#print(a)
print(a.sort())
#print(a)
"""Another Example"""
bikes = ['trek','redline','giant']
first_bike=bikes[0]
print(first_bike)
last_bike=bikes[-1]
print(last_bike)
for bike in bikes:
	print(bike)
bikess=[]
bikess.append('trek')
bikess.append('redline')
bikess.append('giant')
print(bikess)
squares=[]
for x in range(1,11):
	squares.append(x**2)
print(squares)
squaress=[x**2 for x in range(1,11)]
print(squaress)
finishers=['sam','bob','ada','bea']
first_two=finishers[:2]
print(first_two)
copy_of_bikes=bikes[:]
print(copy_of_bikes)
"""Another Example"""
users=['val','bob','mia','ron','ned']
first_user=users[0]
second_user=users[1]
last_user=users[-1]
print(first_user,second_user,last_user)
print(users)
users[0]='valerie'
users[-2]='ronald'
print(users)
users.append('amy')
print(users)
users=[]
users.append('val')
users.append('bob')
users.append('mia')
print(users)
users.insert(0,'joe')
users.insert(3,'bea')
print(users)
del users[-1]
print(users)
users.remove('bea')
print(users)
most_recent_user=users.pop()
print(most_recent_user)
first_user=users.pop(0)
print(first_user)
print(users)
num_users=len(users)
print("We hav "+str(num_users)+" user/s.")
users=[]
users.append('val')
users.append('bob')
users.append('mia')
print(users)
users.sort()
print(users)
users.sort(reverse=True)
print(users)
print(sorted(users))
print(sorted(users,reverse=True))
print(users)
users.reverse()
print(users)
for user in users:
	print(user)
for user in users:
	print("Welcome, "+user+"!")

print("Welcome,we're glad to see you all")