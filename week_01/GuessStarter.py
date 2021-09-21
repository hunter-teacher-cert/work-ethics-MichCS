import random


difference = 0
print("I'm thinking of a number between 0 and a 100 (including both)...")
myNumber = int(input("Select a number Between 0 and a 100 (including both): "))
print("Can you guess my number?:")

yourNumber = random.randint(0, 100)
print(yourNumber)
print("My Number is " + str(myNumber))


if (yourNumber > myNumber):
    difference = yourNumber - myNumber
if (myNumber > yourNumber):
    difference = myNumber - yourNumber

print("You were off by: ")
print(difference)