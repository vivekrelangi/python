def describe_pet(a,n):
    print("\nanimal is "+a)
    print("name is "+n)

describe_pet('hamster','harry')
describe_pet('dog','willie')

describe_pet(a='ham',n='har')
describe_pet(a='dog',n='wil')

def describe_pet1(n,a="dog"):
    print("\nanimal is "+a)
    print("name is "+n)

describe_pet1('harry','hamster')
describe_pet1('dog')

def describe_pet2(a,n=None):
    print("\nanimal is "+a)
    
    if n:
        print("name is "+n)

describe_pet2('hamster','harry')
describe_pet2('snake')