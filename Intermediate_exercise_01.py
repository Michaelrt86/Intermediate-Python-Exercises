def get_unique_list(tempList):
    newList = tempList
    y = 0
    while y < len(newList):
        if newList.count(newList[y]) > 1:
            newList.remove(newList[y])
        if y == len(newList) - 1:
            break
        y = y + 1
    return newList

my_list = [1, 2, 3, 2, 1, 4]
unique_list = get_unique_list(my_list)
print(str(unique_list))