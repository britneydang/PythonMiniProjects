# Choose your own adventure game
# This mini project is about writing my own adventure game.

print('''
*************************************************
================================================.
     .-.   .-.     .--.                         |
    | OO| | OO|   / _.-' .-.   .-.  .-.   .''.  |
    |   | |   |   \  '-. '-'   '-'  '-'   '..'  |
    '^^^' '^^^'    '--'                         |
===============.  .-.  .================.  .-.  |
               | |   | |                |  '-'  |
               | |   | |                |       |
               | ':-:' |                |  .-.  |
               |  '-'  |                |  '-'  |
==============='       '================'       |
*************************************************
''')
print("Welcome to the hungry game!")
print("Your mission is to find food.")

first = input(
    "You are lost in a forest. There is a route. Do you want to turn left or right? Type L for left and R for right. "
)
if first == "L":
    second = input(
        "You found a floatie on the ground and continue to go straight. You see a river. You already have a floatie. Do you want to swim or wait? Type S for swim and W for wait. "
    )
    if second == "W":
        third = input(
            "You hop on a boat and cross the river safely. You got off the boat. Further up the hill there is a building. There are 3 doors - red, yellow, blue - and you will have to choose which one to open first. Type R for red, Y for yellow, and B for blue. "
        )
        if third == "R":
            print(
                "You see a basket of fresh red apples. You take one bite of an apple. You die because of poison. You lose. Game Over!"
            )
        elif third == "B":
            print(
                "You see a glass of iced water. You drink it. You pass out because you are hundry. You lose. Game Over!"
            )
        else:
            print(
                "You see a full table of yummy food. Enjoy your meal. You won!"
            )
    else:
        print(
            "While you are swimming, a crocodile chased after you. You lose. Game Over!"
        )
else:
    print("You got beaten by a brown bear. You lose. Game Over!")
