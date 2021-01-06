class User():
    """ An Attempt to Define a User """

    def __init__(self, first_name, last_name, username, age):
        """ Initialize attributes of class. """
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age
        self.login_attempts = 0
    
    def describe_user(self):
        """ Method to print user information """
        message = f"First: {self.first_name.title()}\n"
        message += f"Last: {self.last_name.title()}\n"
        message += f"Username: {self.username.title()}\n"
        message += f"Age: {self.age.title()}\n"
        print(message)
    
    def greet_user(self):
        """ Print a greeting message to the user. """
        print(f"Hello {self.username} welcome to the Matrix.")

    def increment_login_attempts(self):
        """ Method that increments login attempts each time the method is called. """
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """ Method to reset a users login attempts """
        self.login_attempts = 0

my_user = User("Nathan", "Strickand", "Kilvaari", "33")
my_user.describe_user()
my_user.greet_user()
my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.increment_login_attempts()
print(str(my_user.login_attempts))
my_user.reset_login_attempts()
print(str(my_user.login_attempts))