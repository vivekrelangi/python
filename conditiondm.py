car='bmw'
if car == 'bmw':
    print('y')
else:
    print('n')

car='audi'
if car == 'bmw':
    print('y')
else:
    print('n')

car='Audi'
if car.lower() == 'audi':
    print('y')
else:
    print('n')

toppings='mushrooms'
if toppings!='anchovies':
    print('y')
else:
    print('n')

age=18
if age==18:
    print(True)
if age!=18:
    print(False)

age=19
if age<21:
    print(True)
if age<=21:
    print(True)

a=age>21
print(a)
a=age>=21
print(a)

age_0=22
age_1=18
a=age_0>=21 and age_1>=21
print(a)
age_1=23
a=age_0>=21 and age_1>=21
print(a)

age_0=22
age_1=18
a=age_0>=21 or age_1>=21
print(a)
age_0=18
a=age_0>=21 or age_1>=21
print(a)