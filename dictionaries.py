#Simple Dictionary

alien_0 = {'color': 'green','points': 5}
print(alien_0['color'])
print(alien_0['points'])

#Key Value Pairs 'key': value

#Adding new key value pairs to the dictionary
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#delkey value pair deletion is permanent so be careful

del alien_0['y_position']
print(alien_0)

#Looping through a dictionary
user_0 = {
    'username': 'efermi',
    'first': 'eric',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\n{key}")
    print(f"{value}")

#Looping through only keys of dictionary
print()
favorite_languages = {
    'jen': 'python',
    'sam': 'c',
    'dave': 'c++',
    'kenny': 'java',
    'nathan': 'python',
}

for k in favorite_languages.keys():
    print(k)

#.keys creates list of keys that can then be checked against
print()
#looping through all Keys sorted
for k in sorted(favorite_languages.keys()):
    print(k)

print()
#Looping through all values
for k in favorite_languages.values():
    print(k)

#.keys creates list of keys that can then be checked against
print()
#looping through all Values sorted
for k in sorted(favorite_languages.values()):
    print(k)

#looping through all Values sorted
for k in sorted(favorite_languages.values()):
    print(k)

print()
#looping through all Values sorted setting duplicates need to set first then sort otherise sort fails.
for k in sorted(set(favorite_languages.values())):
    print(k)

#Nesting Dictionaries
print()
#List of Dictionaries
alien_0 = {'color':'green', 'points':5}
alien_1 = {'color':'yellow', 'points':10}
alien_2 = {'color':'red', 'points':25}

aliens = [alien_0,alien_1,alien_2]

print()
for alien in aliens:
    print(alien)

#=============

aliens =[]

#make 30 aliens
for alien_number in range(30):
    new_alien = {'color':'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)

#Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

#Show the number of aliens created
print(f"Total number of aliens: {str(len(aliens))}")