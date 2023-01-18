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
