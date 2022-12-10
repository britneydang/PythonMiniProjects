# RockPaperScissors
# This mini project is my childhood game Rock, Paper, or Scissors.

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

print("Let's play Rock Paper Scissors!\n")

list_of_choices = ["rock", "paper", "scissors"]
player = int(input("Which one do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

if player == 0:
  print(rock)
elif player == 1:
  print(paper)
elif player == 2:
  print(scissors)
else:
  print("You entered an invalid number! Please try again.")
print("You chose " + list_of_choices[player])

computer = random.randint(0,2)
if computer == 0:
  print(rock)
elif computer == 1:
  print(paper)
elif computer == 2:
  print(scissors)
else:
  print("Run into error! Please try again.")
print("Computer chose " + list_of_choices[computer] + "\n")

#Rules
if player == 0 and computer == 0:
  print("2 Rocks. We have a tie!")
if player == 0 and computer == 1:
  print("Paper wins against Rock. You win!")
if player == 0 and computer == 2:
  print("Rock wins against Scissors. You win!")

if player == 1 and computer == 0:
  print("Paper wins against Rock. You win!")
if player == 1 and computer == 1:
  print("2 Papers. We have a tie!")
if player == 1 and computer == 2:
  print("Scissors win against Paper. You lose!")

if player == 2 and computer == 0:
  print("Rock wins against Scissors. You lose!")
if player == 2 and computer == 1:
  print("Scissors win against Paper. You win!")
if player == 2 and computer == 2:
  print("2 Scissors. We have a tie!")


