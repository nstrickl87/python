class Restaurant():
    """ 
    Class Used to Represent a Restaurant
    """

    def __init__(self, restaurant_name, cuisine_type):
        """ Initialize attributes of class. """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """
        Pretty Name to Describe Restaurant
        """
        string1 = f"Welcome to {self.restaurant_name} serving the best"
        string2 = f" {self.cuisine_type} in town!"
        return string1 + string2
    
    def open_restaurant(self):
        """
        Prints Restaurant is open
        """
        print(f"{self.restaurant_name} is now open.")

my_restaurant = Restaurant("Nates", "Breakfast")
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)

print(my_restaurant.describe_restaurant())
my_restaurant.open_restaurant()
