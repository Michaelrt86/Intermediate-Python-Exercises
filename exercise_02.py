print('Enter a string: ')
tempString = input()
print('Enter another string: ')
tempString2 = input()

if tempString2.find(tempString) != -1:
    print ('True')
else:
    print ('false')
