import random

def printChoice(choice):
    """ Choice Acii Printing """
    if choice == 0:
        print("""
            _______
        ---'   ____)
               (_____)
               (_____)
                (____)
        ---.  __(___)
        \n""")
    elif choice == 1:
        print("""
                _______
        ------'    ____)____
                      ______)
                     _______)
                     _______)
        --- .  __________)
        \n""")
    elif choice == 2:
        print("""
                _______
            ---'    ____)____
                       ______)
                   __________)
                   (____)
            ---.__ (___)
       \n """)

#Game Logic
def game_results(user_choice, computer_choice):
    """ Game Logic for Rock Paper Scissors """
    if user_choice == computer_choice:
        print("Tie\n")
    elif user_choice == 0 and computer_choice == 2:
        print("You win.\n")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose.\n")
    elif computer_choice > user_choice:
        print("You lose.\n")
    elif user_choice > computer_choice:
        print("You win.\n")
    else:
        print("Incorrect user input.\n")

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)

printChoice(user_choice)
print("Computer chose:")
printChoice(computer_choice)
game_results(user_choice,computer_choice)
