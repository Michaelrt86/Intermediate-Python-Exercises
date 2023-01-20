#Module 2 Exercise 1
#Write a script that takes in a string from the user. Print the string out backwards.

print('Enter a String: ', end= "")
userInput = input()
userInput = userInput[::-1]
print(userInput)