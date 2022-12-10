# BMICalculator
# This mini project is a BMI calculator

height = input("What is your height? Enter height in m: ")
weight = input("What is you weight? Enter weight in kg: ")

BMI = int(weight)/float(height) ** 2
BMI_round = int(BMI)
print(BMI_round)