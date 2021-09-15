import random

def simple_list_counter():
    """ Simple function that chooses a random number between 0 and 9 inclusive 1000 times and tallies results """
    number_range = list(range(10))
    random_results = []

    for i in range(1000):
        random_choice = random.choice(number_range)
        random_results.append(random_choice)
        
    for number in number_range:
         print(f"{number} has been pulled {random_results.count(number)} times")
    print("\n")

#list_counter()

def useful_list_counter(list_to_pull=None, number_of_pulls=1000, list_weights=[0]):
    """ More Useful Function used to Randomly Select Inclusive Values X Number of Times  and tally the results"""
    random_results = [] #List to store selections

    if list_to_pull == None: #If no list parameter then use default inclusive list
        list_to_pull = list(range(10))
    if number_of_pulls == None: # If no number of pulls parameter do 1000 pulls.
        number_of_pulls = 1000

    if len(list_weights) == len(list_to_pull): # If weight and pull list are same length random pull weighted list
        random_results = random.choices(list_to_pull, list_weights, k=number_of_pulls)
        
        for item in list_to_pull: #Loop through each item in parmeter list and count occurences
            print(f"{item} has been pulled {random_results.count(item)} times")
        print("\n")
    
    else:
        for i in range(number_of_pulls): # Loop based on number of pull parameters.
            random_pull = random.choice(list_to_pull) #randomly choose item from parameter list
            random_results.append(random_pull) # append pull to results list
            
        for item in list_to_pull: #Loop through each item in parmeter list and count occurences
            print(f"{item} has been pulled {random_results.count(item)} times")
        print("\n")

l1 = ["Item 1", "Item 2", "Item 3"]
weights = [10, 30, 60]
l2 = list(range(20))

simple_list_counter()
useful_list_counter(l1, 100, weights)
useful_list_counter(l1,100)
useful_list_counter(l1)
useful_list_counter()

