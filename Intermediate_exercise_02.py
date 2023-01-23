def get_combined_dict(list1, list2):
    thirdDict = {}

    counter = 0
    for key in my_dict_1.keys():
        keyValue = my_dict_1[key]
        for key2 in my_dict_2.keys():
            keyValue2 = my_dict_2[key2]
            if(key == key2):
                thirdDict[key] = keyValue + keyValue2
    
    
    return thirdDict

#my_List_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
#my_List_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}

my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)