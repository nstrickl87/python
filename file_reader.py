with open('Classes/pi.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

print()
file_path = 'Classes/pi.txt'
with open(file_path) as file_object:
    for line in file_object:
        print(line)

print()
file_path = 'Classes/pi.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print((pi_string))
print(str(len(pi_string.strip())))

birthday = input("Enter your birthday, in the form of mmddyy: ")
if birthday in pi_string:
    print("You birthday appears in the first million digits of pi.")
else:
    print("Your birthday does not appear in the first million digits of py.")