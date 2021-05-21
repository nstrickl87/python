import string, random

def random_character(characters, number_of_characters):
    """ Function to choose a random character """
    selection=""
    for char in range(1, number_of_characters + 1):
        random_character = random.choice(characters)
        selection += random_character
    
    return selection

#allowed_symbols = [int(item) for item in input("Enter the list items : ").split()] 
symbols = string.punctuation
letters = string.ascii_letters
digits = string.digits

#print(allowed symbols)

print("Welcome to the PyPassword Generator!")
number_of_letters = int(input("How many letters would you like?\n"))
number_of_symbols = int(input("How many symbols would you like?\n"))
number_of_numbers = int(input("How many numbers would you like?\n"))

password = ""

password += random_character(letters, number_of_letters)
password += random_character(symbols, number_of_symbols)
password += random_character(digits, number_of_numbers)

random_password = list(password)
random.shuffle(random_password)
shuffled_password =''.join(random_password)

print(f"Unshuffled Random Password: {password}")

print(f"Total Random Password: {shuffled_password}")