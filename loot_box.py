import random

# Takes Weighted List Pairings and Choose One Randomly
def random_choice(choice_list):
    """ Used to build choices based on weight """
    list = []
    for item, weight in choice_list:
        list.extend( [item]*weight )
    return random.choice((list))

# Open Chest Function
def open_chest(tier_list,pity_list,num_pulls,player_inventory):
    """ Opens Chest """
    items_received = [] # used keep to track of item pulls per open
    obtained_tier4 = [] # used to track unique obtained tier4 items
    reroll_tier4_list = pity_list[:] # Sliced Copy of Pity List or T4 Loot List

    for x in range(1,num_pulls+1):
        tier_roll = random_choice(tier_list) # Roll for tier of item
        item_roll = random_choice(tier_roll) # Roll for item within tier
        items_received.append(item_roll) # Append Item to tracking list

    for item in items_received:
        if 'T4' in item and item not in player_inventory: #check each item to see if it is T4 and has not been added to player inventory
            obtained_tier4.append(item) # Append T4 item to tracking obtained T4 list
            reroll_tier4_list = list(set(pity_list) - set(obtained_tier4)) # Build reroll list to prevent for duplicate check
        elif 'T4' in item and item in player_inventory: # check item to see if already in inventory
            if float(len(obtained_tier4))<float(len(pity_list)/2): #check to see if player has obtained 50% of T4 Items if not remove 
                items_received.remove(item) #If not at below 50% remove item
                items_received.append(random_choice(reroll_tier4_list)) #reroll item from reroll list
    return items_received

def tier4_items_count(player_inventory):
    """ counts the number of T4 Items a Player has """
    count = 0
    for string in player_inventory:
        if "T4" in string:
            count += 1
    return count

number_of_chests_open = 0 #Tracker for total chests 
pity_chest_counter = 0 #Tracker for total chests open since last Tier 4 item received
player_number_of_tier4_items = 0 #Value to 
player_inventory = []

#Item, Weight Pairings for each Tier
loot_tier1 = [ ('T1-Item_1',25), ('T1-Item_2',25), ('T1-Item_3',25), ('T1-Item_4',25)]
loot_tier2 = [ ('T2-Item_1',40), ('T2-Item_2',40), ('T2-Item_3',20)]
loot_tier3 = [ ('T3-Item_1',40), ('T3-Item_2',40), ('T3-Item_3',20)]
loot_tier4 = [ ('T4-Item_1',20), ('T4-Item_2',20), ('T4-Item_3',20), ('T4-Item_4',20), ('T4-Item_5',20) ]


pity_choice = [(loot_tier4,100)] # List to ensure reroll on T4 Item
tier_choice = [(loot_tier1,5000), (loot_tier2,4000), (loot_tier3,900), (loot_tier4,10)] # Tier, Weight pairings of loot tiers.

chest_session = True
while chest_session:

    user_choice = input("Open Chest Enter or q to quit):")
    if user_choice == 'q':
        print(f"Number of Chests Opened:{number_of_chests_open}")
        print(f"Pity Counter:{pity_chest_counter}")
        print(f"This is the Current Players Inventory:\n{player_inventory}")
        print(f"Number of Tier 4 Items Obtained:{tier4_items_count(player_inventory)}")
        break
    else:

        current_tier4_items_count = tier4_items_count(player_inventory)
        number_of_chests_open += 1
        pity_chest_counter += 1
        
        if pity_chest_counter < 20: # If Pity Counter is Less than 20 Open Chest
            player_inventory.extend(open_chest(tier_choice,loot_tier4,3,player_inventory))
        elif pity_chest_counter > 19: #If Pity Counter Greater than 19 
            pity_chest_counter = 0 #Reset Pity Time
            player_inventory.extend(open_chest(pity_choice,loot_tier4,1,player_inventory)) #Force 1 pull from T4
            player_inventory.extend(open_chest(tier_choice,loot_tier4,2,player_inventory)) #Perform 2 Remaining Pulls
        
        if current_tier4_items_count < tier4_items_count(player_inventory):
            pity_chest_counter = 0 # Check to make sure no new T4 were added, other wise reset pity

        tier4_items_count(player_inventory)
        # Print Chest/Pity/Inventory/Number of T4 Items for Reference.
        print(f"Number of Chests Opened:{number_of_chests_open}")
        print(f"Pity Counter:{pity_chest_counter}")
        print(f"This is the Current Players Inventory:\n{player_inventory}")
        print(f"Number of Tier 4 Items Obtained:{tier4_items_count(player_inventory)}")