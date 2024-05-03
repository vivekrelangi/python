class car:
    """a = 7
    def disp():
        print(a)"""
    def __init__(self,modelname,year):
        self.modelname=modelname
        self.year=year
    def display(self):
        print(self.modelname,self.year)

c=car("TATA",2000)
c.display()
class Dog():
    """Represent a dog."""
    def __init__(self,name):
        """Initialize dog object"""
        self.name=name
    def sit(self):
        """Simulate sitting."""
        print(self.name + " is sitting.")
my_dog = Dog('Peso')
print(my_dog.name + " is a great dog!")
my_dog.sit()