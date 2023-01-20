#Exercise 07
#Take in integers until the user types "QUIT" and store the numbers in a list. 
# Assume any input other than "QUIT" is a valid integer. Create another list of just the even numbers and print both lists.
numList = []
evenList = []
userInput = 0


while userInput != 'QUIT':
    print('Enter a number or QUIT to quit: ', end= "")
    userInput = input()
    if userInput == 'QUIT':
        break
    
    numList.append(int(userInput))
    if int(userInput) % 2 == 0:
        evenList.append(int(userInput))

print('All Nums:', numList)
print('Even Nums:', evenList)