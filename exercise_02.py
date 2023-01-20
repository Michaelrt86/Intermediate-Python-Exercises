#Exercise 02
#Write a script that takes in two strings from the user. If one string is the suffix of the other string, print "True", otherwise, print "False". For example, 
# if the user enters "brush" and "paintbrush", then the script would print "True". If the user entered "painting" and "painted", 
# the script would print "False" because no string ends with the other. 
#  in mind that the the pair "brush" and "paintbrush" as well as the pair "paintbrush" and "brush" would print "True" because order does not matter.

print('Enter a string: ')
tempString = input()
print('Enter another string: ')
tempString2 = input()

if tempString2.find(tempString) != -1:
    print ('True')
else:
    print ('false')
