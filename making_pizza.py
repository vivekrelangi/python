"""Importing an entire module"""
#import pizza
#pizza.make_pizza('medium','pepperoni')
#pizza.make_pizza('small','bacon','pineapple')
#importing specific function
#from pizza import make_pizza
#make_pizza('medium','pepperoni')
#make_pizza('small','bacon','pineapple')
#giving a module as an alias
"""import pizza as p
p.make_pizza('medium','pepperoni')
p.make_pizza('small','bacon','pineapple')"""
#giving a function as an alias
"""from pizza import make_pizza as mp
mp('medium','pepperoni')
mp('small','bacon','pineapple')"""
from pizza import *
make_pizza('medium','pepperoni')
make_pizza('small','bacon','pineapple')


