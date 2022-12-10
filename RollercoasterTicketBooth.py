# RollercoasterTicketBooth
# This mini project is about a roller ticket seller whom responsible to check rider's height and sell ticket.

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print("You can ride the roller coaster!")
    age = int(input("How old are you? "))
    if age < 12:
        bill = 5
        print("Child ticket is $5.")
    elif age <= 18:
        bill = 7
        print("Youth ticket is $7.")
    elif age >= 45 and age <= 55:
        bill = 0
        print("If you are in the Midlife age, the ticket is on us.")
    else:
        bill = 12
        print("Adult ticket is $12.")

    photo = input("Do you want photo for $3? Y or N? ")
    if photo == "Y":
        bill = bill + 3

    print(f"Your total bill is ${bill}.")
else:
    print("Sorry, you have to grow taller.")
