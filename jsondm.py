"""Store some numbers"""
import json
numbers = [0,1,2,3,4,5,6,7,8,9]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

"""Load some previously stored numbers"""
#import json
filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)

"""Making sure the stored data exists"""
#import json
f_name = 'numbers1.json'
try:
    with open(f_name) as f_obj:
        numbers = json.load(f_obj)
except FileNotFoundError:
    msg = "Can't find {0}".format(f_name)
    print(msg)
else:
    print(numbers)