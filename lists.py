bicycle = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycle)

#Accessing Elementals in  list
print(bicycle[0])

#Title Accessing
print(bicycle[0].title())

#Accessing Last Element in List -2 returns the second to last item from the end of the list
print(bicycle[-1])

#using individual values from a list
message = "My first bicycle was a " + bicycle[0].title() + "."
print(message)

#Modifying Elements in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

#Adding Elements to a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

#Build Lists Dynamically
new_motorcycles =[]

new_motorcycles.append('honda')
new_motorcycles.append('yamaha')
new_motorcycles.append('suzuki')

print(new_motorcycles)

#inserting Values into a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)

#Removing an item using the del statement
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

#Removing an Item Using the pop() method
# pop lets you remove the last item of the list and use it after removing it.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#you can also pop from a deisred place within a list
motorcycles = ['honda', 'yamaha', 'suzuki']#Assume list is chronological and want to list first bike owned
first_motorcycle = motorcycles.pop(0)
print(first_motorcycle)

#removing an item by value if I do not know position but value I would like to remove
# can also use variable to store value and check in remove.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles)

#Organizing a list 
# Sorting a List Permanently witht he Sort() Method
cars  = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

#Can Sort in revers order
cars  = ['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)

#Sorting a List Temporarily with the Sorted() Function
cars  = ['bmw','audi','toyota','subaru']

print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\n`Here is the original list again:")
print(cars)

#Printing a list in reverse order
cars  = ['bmw','audi','toyota','subaru']
print(cars)
cars.reverse()
print(cars)

#Finding the length of a list
cars  = ['bmw','audi','toyota','subaru']
print(len(cars))

