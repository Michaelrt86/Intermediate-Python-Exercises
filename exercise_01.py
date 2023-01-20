#Exercise 01
#Write a script that takes in a grade from 0-100 inclusive (include both 0 and 100 in the range). 
# Assuming a normal 10 point grading scale, print off whether the user got an A, B, C, D, or F.

print('Please enter in your grade')
givenGrade = int(input())
grade = 'F'
if givenGrade >= 90:
    grade = 'A'
elif givenGrade >= 80:
    grade = 'B'
elif givenGrade >= 70:
    grade = 'C'
elif givenGrade >= 60:
    grade = 'D'
else:
    grade = 'F'
print ('Your grade is ' + grade)
