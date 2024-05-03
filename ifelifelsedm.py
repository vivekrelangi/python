age=19
if age>=18:
    print("You're old enough to vote!")

age=17
if age>=18:
    print("You're old enough to vote!")
else:
    print("You can't vote yet")

age=12
if age<4:
    price=0
elif age<18:
    price=5
else:
    price=10
print("Your cost is "+str(price)+" rupees.")