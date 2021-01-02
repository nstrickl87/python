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

new_motorcycles.append('womdwd')

print(new_motorcycles)



