#important python library called random

import random

#initialize difference
#ask for input from user
difference = 0
print("I'm thinking of a number between 0 and a 100 (including both)...")
myNumber = int(input("Select a number Between 0 and a 100 (including both): "))
print("Can you guess my number?:")

#initialize and declare at once (random integer)
yourNumber = random.randint(0, 100)
print(yourNumber)
print("My Number is " + str(myNumber))

#add if statements
if (yourNumber > myNumber):
    difference = yourNumber - myNumber
if (myNumber > yourNumber):
    difference = myNumber - yourNumber

print("You were off by: ")
print(difference)