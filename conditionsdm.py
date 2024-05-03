x=42
a=x==42
b=x!=42
c=x>42
d=x>=42
e=x<42
f=x<=42
bikes=['trek']
g='trek' in bikes
h='surly' not in bikes
game_active=True
can_edit=False
age=18
if age >= 18:
    print("You can vote")
else:
    print("You can not vote")
if age<4:
    ticket_price=0
elif age<18:
    ticket_price=10
else:
    ticket_price=15
print(ticket_price)
print(a,b,c,d,e,f,g,h,game_active,can_edit,end=" ") 