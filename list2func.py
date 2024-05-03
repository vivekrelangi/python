def greet_users(names):
    for name in names:
        msg = "Hello, " + name + "!"
        print(msg)

usernames=['hannah','ty','margot']
greet_users(usernames)

def print_models(unprinted,printed):
    while unprinted:
        current_model=unprinted.pop()
        print("Printing "+current_model)
        printed.append(current_model)

unprinted=['phone case', 'pendant', 'ring']
printed=[]
print_models(unprinted,printed)

print("\nUnprinted:",unprinted)
print("Printed:", printed)

original=['phone case', 'pendant', 'ring']
printed=[]
print_models(original[:],printed)

print("\nOriginal:",unprinted)
print("Printed:", printed)