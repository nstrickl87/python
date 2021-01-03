cars = ['audi','hyundai','honda','ford']

for car in cars:
    if car == 'hyundai':
        print(car.title())

#Checking for inequality
requested_car_maker = 'hyundai'

for car in cars:
    if car != requested_car_maker:
        print("This is not the car you are looking for!")
    else:
        print("We found your " + car.title() + "!")

#Checking Multiple Conditions
age_0 = 22
age_1 = 12

print(age_0 >= 21 or age_1 >= 21)

# Checking to see if a value is within a list.
toppings = ['mushrooms', 'peppers', 'onions', 'pineapple']
print('pineapple' in toppings)

requested_topping = 'pepperoni'
if requested_topping not in toppings:
    print(requested_topping.title() + " not available!")

# If elif else 
user_age = 13

if user_age < 4:
    print("Your admission is $0.00")
elif user_age < 18:
    print("Your admission is $5.00")
else:
    print("Your admission is $10.00")


if user_age < 4:
    price = 0
elif user_age < 18:
    price = 5
else:
    price =10
print(f"You price of admission is ${price}.")

#Python does nto require else statement and may end with elif for catching specific last case

#Checking if a list is Not Empty

requested_topping = []

if requested_topping:
    print("There is one topping in the list at least.")
else:
    print("There is NO topping in the list.")

# multiple lists check
available_toppings = {'cheese','sausage', 'olives', "peppers"}

for requested_toppings in toppings:
    if requested_toppings in available_toppings:
        print(f"Adding {requested_toppings.title()} to your pizza.")
    else:
        print(f"Sorry, we don't have {requested_toppings.title()}.")