def functionReturn(tempString):
    userInput = tempString.lower().replace(' ', '')
    print(userInput)
    dictList = {}
    for x in range(0, len(userInput)):
        dictList[userInput[x]] = userInput.count(userInput[x])
    return dictList

print('Enter a string: ', end= '')
userWord = input()
print(functionReturn(userWord))