#Exercise 04
#Take in a number, n, from the user. Then, take in n floats from the user and store them in a list. 
# For instance, if the user enters 4, then the user will have to enter 4 numbers. Print the list and the mean.

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
print ('The',average / counter)