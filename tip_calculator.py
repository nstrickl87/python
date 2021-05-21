print("Welcome to the tip calculator.")
bill_total = input("What was the total bill? $")
percentage_tip = input("What pecentage tip would you like to give? 10, 12, or 15? ")
number_split = input("How many people to splith the bill? ")

bill_total = float(bill_total)
percentage_tip = float(percentage_tip) / 100
number_split = float(number_split)

bill_plus_tip = round((bill_total * (1 + (percentage_tip))),2)

if(number_split > 1):
    split_amount = round((bill_plus_tip / number_split),2)
    print(f"Each person should pay: ${split_amount}\n")
else:
    split_amount = round((bill_plus_tip / number_split),2)
    print(f"You should pay: ${split_amount}\n")