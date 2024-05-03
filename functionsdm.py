def greet_user():
    """Display a single greeting"""
    print("Hello!")

greet_user()
def greet_user(username):
    """Display a personalized greeting"""
    print ("Hello "+username+"!")

greet_user('jesse')
def make_pizza(topping='bacon'):
    """Make a single-topping pizza"""
    print("Have a "+topping+"pizza!")

make_pizza()
make_pizza('pepperoni')
def add_numbers(x,y):
    """Add two numbers and return the sum."""
    return x+y
sum = add_numbers(3,5)
print(sum)