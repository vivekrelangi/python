#import booleanvalsdm
def make_pizza(size, *toppings):
    print("\nMaking a " + size + " pizza.")
    print("Toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('small','pepperoni')
make_pizza('large','bacon bits', 'pineapple')
make_pizza('medium','mushrooms','peppers','onions','extra cheese')

def build_profile(first, last, **user_info):
    profile={'first':first, 'last':last}

    for key,value in user_info.items():
        profile[key]=value

    return profile
user_0=build_profile('albert','einstein',location='princeton')
user_1=build_profile('marie','curie',location='paris',field='chemistry')

print(user_0)
print(user_1)
