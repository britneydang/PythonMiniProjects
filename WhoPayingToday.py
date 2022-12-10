# WhoPayingToday
# This mini project is about selecting randomly a person in a group will pay for the total bill.

import random

names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")

qty = len(names)
random_choice = random.randint(0, qty - 1)
random_name = names[random_choice]

print(f"{random_name} is paying meal for the whole group today!")
