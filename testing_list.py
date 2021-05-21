import random

loot_tier4 = ['T4-Item_1', 'T4-Item_2', 'T4-Item_3', 'T4-Item_4', 'T4-Item_5']

temp_loot_tier4 = loot_tier4[:]

player_inventory = ['T3-Item_2', 'T2-Item_1', 'T1-Item_1', 'T2-Item_2', 'T1-Item_1', 'T3-Item_3']
obtained_tier4 = []

roll = loot_tier4[random.randint(0,4)]

open_session = True

while open_session:
    user_input = input("Press Enter to Continue")

    if(user_input == 'q'):
        break
    else:
        roll = loot_tier4[random.randint(0,4)]
        print(roll)

        if 'T3' in roll:
            if roll not in player_inventory:
                player_inventory.append(roll)
                obtained_tier4.append(roll)
                temp_loot_tier4.remove(roll)

            elif roll in player_inventory and round(len(loot_tier4)/2) >= len(obtained_tier4):
                new_roll = temp_loot_tier4[random.randint(0,len(temp_loot_tier4))]
                player_inventory.append(new_roll)
                obtained_tier4.append(new_roll)
                temp_loot_tier4.remove(new_roll)
            else:
                player_inventory.append(roll)
                
            print(round(len(loot_tier4)/2) >= len(obtained_tier4))
            print(player_inventory)



            for item in items_received:
        if "T4" in item:
            for item in player_inventory:
                if item not in player_inventory:
                    obtained_tier4.append(item)
                    copy_loot_tier4.remove(item)
                elif item in player_inventory and round(len(loot_tier4)/2) >= len(obtained_tier4):
                    items_received.remove(item)
                    new_roll = copy_loot_tier4[random.randint(0,len(copy_loot_tier4))]
                    items_received.append(new_roll)
                    obtained_tier4.append(new_roll)