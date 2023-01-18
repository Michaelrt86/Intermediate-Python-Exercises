#firstList = []
firstList = [1,2,3,4,5]
#secondList = []
secondList = [6,7,8,9,1]
thirdList = []

"""""
for x in range(10):
    if x < 5:
        print('please enter a number for the first list',x + 1,end= " ")
        firstList.append(int(input()))
    else:
        print('please enter a number for the second list',x + 1,end= " ")
        secondList.append(int(input()))
print (firstList)
print (secondList)
"""""
thirdList.extend(firstList)
thirdList.extend(secondList)

for x in range(0,len(thirdList)):
    for y in range(0, len(thirdList)):
        if thirdList[x] == thirdList[y]:
            thirdList.pop(y)
print(thirdList)