import random

class Dice():
    """ Class Used to Simulate Rolling Dice """

    def __init__(self, sides=6):
        """ Initialize attributes of class. """
        self.sides = sides
    
    def roll_dice(self):
        """ Function to Roll Dice """
        roll = random.randint(1,self.sides)
        print(str(roll))
    
    def num_rolls(self, times):
        for x in range(0, times):
            self.roll_dice()
            x += 1

d6_dice = Dice()
d6_dice.num_rolls(10)
print()
d10_dice = Dice(10)
d10_dice.num_rolls(10)
print()
d20_dice = Dice(20)
d20_dice.num_rolls(10)