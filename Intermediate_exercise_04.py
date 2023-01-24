x = 1
sum = 0
while x in range(1,6):
    print('Enter int #',x, end= ': ')
    userInput = input()
    if userInput.isdigit():
        tempInt = int(userInput)
        sum = sum + tempInt
        x = x + 1
    else:
        print('Invalid input. Please enter an int. ')

print('Your sum is ' + str(sum))