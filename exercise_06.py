#Exercise 06
#Take in a row number from 1 to 5 inclusive and a column number from 1 to 5. Print out a grid of 0s, but in the row and column entered by the user, print a 1.

matrix = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
print('Enter a row num from 1 to 5: ', end= "")
firstNum = int(input())-1
print('Enter a col num from 1 to 5: ', end= "")
secondNum = int(input())-1

matrix[firstNum][secondNum] = 1

for x in range(0,5):
    for y in range(0,5):
        print(matrix[x][y], end= " ")
    print()