# Name: Raycan2849
# Date: November 5, 2026
# Description: This program asks the user for their information, plays a number guessing game 
# using while loops and if/else decision structures, and outputs incremented values using loops.

userName = input("What is your name? ")
studentId = input("What is your studentID? ")

secretNumber = 5
numberOfTries = 0
userGuess = 0

# Number guessing game loop
while userGuess != secretNumber:
    userGuess = int(input("Please guess a number between 1 and 10..."))
    numberOfTries += 1
    
    if userGuess < secretNumber:
        print("You guessed too low")
    elif userGuess > secretNumber:
        print("You guessed too high")
    else:
        print(f"Congratulations, {userName}! You guessed the number in {numberOfTries} tries!")

# While loop output
print("\nOutput from the 'while' loop:")
loopCounter = 0
while loopCounter < 5:
    incrementValue = loopCounter + 1
    print(f"{secretNumber} incremented by {incrementValue} is {secretNumber + incrementValue}")
    loopCounter += 1

# For loop output
print("\nOutput from the 'for' loop:")
for i in range(5):
    incrementValue = i + 1
    print(f"{secretNumber} incremented by {incrementValue} is {secretNumber + incrementValue}")