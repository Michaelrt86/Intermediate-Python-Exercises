print('Enter a number: ' , end= " ")
counter = int(input())
intList = []
average = 0
for item in range(0, counter):
    print('Enter number ', item + 1, end = " ")
    userChoice = float(input())
    intList.append(userChoice)
    average += userChoice

print('List:',intList)
print ('Average:',average / counter)