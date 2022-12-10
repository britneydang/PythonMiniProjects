# TipCalculator
# This mini project is about calculating a splitted amount including tip for a group

print("Welcome to the tip calculator!")

bill = float(input("What is total bill? $"))
tip = int(input("How many percent for tip? 10, 12, or 15? "))
people = int(input("How many people are splitting the bill? "))

bill_with_tip = tip/100 * bill + bill
bill_splitting = round(bill_with_tip / people,2)

#Format the result to 2 decimal places
final_amount = "{:.2f}".format(bill_splitting)
print(f"Each person should pay {final_amount} dollars.")