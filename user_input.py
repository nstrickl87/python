#How the input function works
message = input("Tell me something, and I will repeat it.")
print(message)

#Input function should be written with clear and concise directions.

#Modulo Operator

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

#while loop
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

#Letting user choose when to quit.
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = ""

while message != 'quit':
    message = input(prompt)
    print(message)