file_path = 'Classes/programming.txt'

with open(file_path, 'w') as file_object: #Important to note that writing to a file that already exists clears the file. Append using 'a' instead
    file_object.write("I love programming!\n")
    file_object.write("I really really like to program in Python.")
    
def add_to_guest_list(name, guest_list): #Could also pass in filepath for guest list
    """ Function to add a guest to the guests.txt file """
    with open(guest_list, 'a') as file_object:
        file_object.write(f"{name}\n")

def read_guest_list(guest_list):
    """ Read a Guest List """
    with open(guest_list, 'r') as file_object:
        lines = file_object.readlines()
    for line in lines:
        print(line.strip())

guest_book_open = True


file_path_guest_book = 'Classes/guests_book.txt'
while guest_book_open:
    guest = input("Please let me know you name so that I can add it to the guest list: ")
    if guest == 'done':
        guest_book_open = False
        print("You have registered the following guests:")
        read_guest_list(file_path_guest_book)
    else:
        add_to_guest_list(guest,file_path_guest_book)
        print(f"Welcome {guest}.")
