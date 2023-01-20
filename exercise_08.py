#Exercise 08
#Take in 10 integers from user. Create a new list with only elements which appear once. Print both lists.

numList = []
onceList = []

for x in range(0,10):
    print('Enter number ' + str(x + 1) + ": ", end= " ")
    userInput = int(input())
    numList.append(userInput)

for y in range(0,10):
    if numList.count(numList[y]) == 1:
        onceList.append(numList[y])
print('Original List: ' + str(numList))
print('Nums that appear once: ' + str(onceList))