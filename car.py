class Car():
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

class Battery():
    def __init__(self,size=70):
        self.size=size
        self.charge_level=0

    def get_range(self):
        if self.size == 70:
            return 240
        elif self.size==85:
            return 270
        
class ElectronicCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)

        #self.battery_size = 70
        #self.charge_level = 0
        self.battery = Battery()


    def charge(self):
        self.charge_level = 100
        print("The vehicle is fully charged.")