#Module 2 Exercise 2
#Write a script that takes in a string from the user. Print the string where all the lower case letters are shifted to the front and the spaces removed. 
# Keep the relative order of the lower case letters and upper case letters.
upperCase = ''
lowerCase = ''
print('Enter a string: ', end= "")
userInput = input()

x = 0
while x < len(userInput):
    if userInput[x].isupper():
        upperCase = upperCase + userInput[x]
    else:
        lowerCase = lowerCase + userInput[x]
    x = x + 1

userInput = (lowerCase + upperCase).replace(' ', '')
print(userInput)