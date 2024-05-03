from classesdm1 import Car
class ElectronicCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)

        self.battery_size = 70
        self.charge_level = 0

    def charge(self):
        self.charge_level = 100
        print("The vehicle is fully charged.")

    def fill_tank(self):
        print("This car has no fuel tank!")

my_ecar = ElectronicCar('tesla','model s',2016)

my_ecar.charge()
my_ecar.drive()
my_ecar.fill_tank()