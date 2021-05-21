class Car():
    """
    A Simple Attempt to represent a car.
    """
    
    def __init__(self, make, model, year, odometer_reading):
        """ Initialize attributes """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = odometer_reading

    def get_descriptive_name(self):
        """ Return neatly formatted name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """ Print the Cars Odometer """
        print(f"This car has {(str(self.odometer_reading))} mile on it.")
    
    def set_odometer(self,mileage):
        """ Method to Set the Cars Mileage """
        self.odometer_reading = mileage
    
    def update_odometer(self, distance_traveled):
        """ Method used to update a cars given mileage """
        self.odometer_reading += distance_traveled

#Inheritance
class ElectricCar(Car):
    """ Representing aspects of a car, specific to Elecitric vehicles """

    def __init__(self, make, model, year, odometer_reading):
        """ Initialize Attributes """
        super().__init__(make, model, year, odometer_reading)
        self.battery = Battery()


class Battery():
    """ Representing information on batteries for cars """

    def __init__(self, battery_size=70):
        """ Initialize attributes of class. """
        self.battery_size = battery_size

    def describe_battery(self):
        """ Print a statement about the battery size. """
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        """ Method used to prtin statement about approximate range of battery """
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        else:
            range = 0
        
        message = f"This car can go approximately {str(range)}"
        message += " on a full charge."
        print(message)
    
    def upgrade_battery(self):
        """ Upgrade the battery to 85 if not already """
        if self.battery_size == 70:
            self.battery_size = 85
        elif self.battery_size == 85:
            print("Cannot upgrade battery any further.")

my_car = Car("Pontiac", "GTO", 1966, 100)
print(my_car.get_descriptive_name())

my_car.read_odometer()
my_car.set_odometer(2000)
my_car.read_odometer()
my_car.update_odometer(5000)
my_car.read_odometer()

my_tesla = ElectricCar("Tesla","Model Y", 2021, 27)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
print(str(my_tesla.battery.battery_size))
my_tesla.battery.upgrade_battery()
print(str(my_tesla.battery.battery_size))

my_second_tesla = ElectricCar("Tesla", "Model 3", 2021, 12)
my_second_tesla.battery.upgrade_battery()
my_second_tesla.battery.upgrade_battery()

