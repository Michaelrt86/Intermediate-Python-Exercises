#Exercise 10
#Take in a string from the user and split it into an array of single characters. 
# Split the list of characters into a list of lists where each inner list has 3 elements. 
# Notice that the last inner array may have less than 3 elements.

print('Enter a string: ', end= "")
userInput = input()
bigList = []
tempList = []
for x in range(0, len(userInput)):
    tempNum = x +1
    if len(tempList) < 3:
        tempList.append(userInput[x])
    else:
        bigList.append(tempList)
        tempList = [userInput[x]]
bigList.append(tempList)
print(bigList)