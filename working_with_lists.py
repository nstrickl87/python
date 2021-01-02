#Looping Through Lists
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

#More WOrk in a Loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title())

#makign Numerical Lists using the range function
#Range off by one starts counting from first value and stops counting att he second value off by one
for value in range (1,5):
    print(value)

#Print 1  through 5
for value in range (1,6):
    print(value)

#Using range to make a list of Numbers
numbers = list(range(1,6))
print(numbers)

#List only even numbers between 1 and 10
#Starts at 2 and then adds 2 until reaches second value.
even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

#Simple Stats with numbers
digits = list(range(0,10))
print(digits)

print(min(digits))
print(max(digits))
print(sum(digits))

#List Comprehensions a;;pws up to generate this same list in just one line of code. 
squares = [value**2 for value in range (1,11)]
print(squares)

#Slicing and List
#To make a slice you indicate the first and last element you want to work with 
players = ['nathan', 'caitlin','hazel', 'pat','brett','wayland']
print(players[0:3]) #First three elements in the list

#want 2nd 3rd and 4th person in a list
print(players[1:4])

#Without a starting index python assumes the start of the list
print(players[:4])

#Want all items in a list starting formt eh second item
print(players[1:])

#Negative index returns an element a certain distance from the end of the list
# Return last 3 players from listaZ
print(players[-3:])

#Looping through a slice
print("Last 3 players in the list:")
for name in players[-3:]:
    print(name)

#Copying a List
family = players[:]
print(players)
print(family)

#Tupule
print("\n======== Tuples ========\n\n")
#Lists Work Well for storing sets of items that can change throughout the life of a program. The ability to modify lists is particularly 
# Lists good for list of users on a website or a list of characters in a game.
#Sometimes  we wantt ot create a list of items that cannot change Tuples allow for this.
#Python referes to values that cannot change as immutable. An Immutable list is a tuple

dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

#Tuples are defined with () instead of the []

#Looping through Tuple
for dimension in dimensions:
    print(dimension)

#Writing over a Tuple
#Although you cannot modify a Tuple., You can assign a new value to a variable that holds a tuple.
#So if we wanted to redefine the tuple we can

print("Oringinal Dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)

print("New Dimensions")
for dimension in dimensions:
    print(dimension)

#use tuples when we do not want values to change in a program as they are a simple data structure.

