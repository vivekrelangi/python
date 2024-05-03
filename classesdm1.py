class Car():
    """A simple attempt to model a car."""

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_capacity = 15
        self.fuel_level = 0

    def fill_tank(self):
        self.fuel_level=self.fuel_capacity
        print("Fuel tank is full.")

    def drive(self):
        print("The car is moving")

    def update_fuel_level(self,new_level):#updating an attribute value
        if new_level <= self.fuel_capacity:
            self.fuel_level = new_level
        else:
            print("The tank can't hold that much!")

    def add_fuel(self,amount):
        if (self.fuel_level + amount <= self.fuel_capacity):
            self.fuel_level += amount
            print("Added fuel")
        else:
            print("The tank won't hold that much.")

"""c=Car('car','bmw',2000)
#c('car','bmw',2000)
c.fill_tank()
c.drive()"""
my_car=Car('audi','a4',2016)
print(my_car.make)
print(my_car.model)
print(my_car.year)
"""my_car.fill_tank()
my_car.drive()
my_new_car = Car('audi','a4',2016)
my_new_car.fuel_level=5#int(input("Fill fuel:"))
f=int(input("Fill fuel:"))
my_new_car.update_fuel_level(f)
my_new_car.add_fuel(17)"""