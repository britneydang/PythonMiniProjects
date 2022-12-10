# AverageHeightCalculator
# This mini project is about calculate the average height of many students using for loop

print("Calculate average of students' heights!\n")

student_heights = input("Type a list of student heights - Add a space between, no comma needed.").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

#Find the total height of all students - not using sum, use for loop only
total_heights = 0
for height in student_heights:
  total_heights = total_heights + height
print(total_heights)

#Find the number of students - not using len, use for loop only
total_students = 0
for student in student_heights:
  total_students = total_students + 1
print(total_students)

#Average and round 
average_heights = round(total_heights/total_students)
print(average_heights)

print(f"The average heights of {total_students} students is {average_heights}.")
