import random
print("Guess a number between 1 to 10")
MIN = 1
MAX = 10

targetNumber = random.randint(MIN, MAX)
#print(targetNumber)

guessedNumber = input("your guess")

if targetNumber == guessedNumber :
    print("Yay! you guessed correct")
else :
    print("Oops! wrong guess")
