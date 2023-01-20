#Exercise 09
#Take in 5 words from the user and store them in a list. Then, create a single string from the individual words, 
# separated by spaces, and print the list and resultant string.
wordList = []
completeString = ''

for x in range(0,5):
    print('Enter a word: ', end= "")
    userInput = input()    
    wordList.append(userInput)
    completeString = completeString + userInput + " "
print('Words: ' + str(wordList))
print('One String: ' + str(completeString))
