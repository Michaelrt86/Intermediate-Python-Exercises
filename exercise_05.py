#Exercise 05
#Take in 5 integers from the user and store them in a list. Then take in another 5 integers and store them in a separate list. 
# Create a third array containing the common values from both arrays without duplicates. Print out all three lists.

firstList = []
#firstList = [1,2,1,4,7]
secondList = []
#secondList = [6,7,8,9,1]
thirdList = []


#CREATION OF THE ARRAYS
#"""""
for x in range(10):
    if x < 5:
        print('please enter a number for the first list', end= " ")
        firstList.append(int(input()))
    else:
        print('please enter a number for the second list', end= " ")
        secondList.append(int(input()))
print (firstList)
print (secondList)
#"""""

#LOOPING SECTION CHECKING FOR PAIRS BETWEEN BOTH LISTS THEN ADDING THEM TO THE THIRDLIST
size = len(thirdList)
for x in range(0,5):
    for y in range(0, 5):
        if firstList[x] == secondList[y]:
            thirdList.append(firstList[x])
            break
#CHECKING FOR DUPLICATES IN THIRDLIST AND REMOVING IF FOUND
#"""""
z = 0
while z < len(thirdList):
    if thirdList.count(thirdList[z]) > 1:
        thirdList.remove(thirdList[z])
        z = z + 1
    if z == len(thirdList) - 1:
        break    
#"""""
print(thirdList)