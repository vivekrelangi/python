class Battery():
    def __init__(self,size=70):
        self.size=size
        self.charge_level=0

    def get_range(self):
        if self.size == 70:
            return 240
        elif self.size==85:
            return 270

from classesdm1 import Car
class ElectronicCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)

        #self.battery_size = 70
        #self.charge_level = 0
        self.battery = Battery()


    def charge(self):
        self.charge_level = 100
        print("The vehicle is fully charged.")

my_ecar = ElectronicCar('tesla','model x',2016)
my_ecar.charge()
print(my_ecar.battery.get_range())
my_ecar.drive()