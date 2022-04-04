"""
Guess the Number

The Goal: Similar to the first project, this project also uses the random module in Python. The 
program will first randomly generate a number unknown to the user. The user needs to guess what that 
number is. (In other words, the user needs to be able to input information.) If the user’s guess is 
wrong, the program should return some sort of indication as to how wrong (e.g. The number is too high
or too low). If the user guesses correctly, a positive indication should appear. You’ll need 
functions to check if the user input is an actual number, to see the difference between the inputted 
number and the randomly generated numbers, and to then compare the numbers.
Concepts to keep in mind:

Random function
Variables
Integers
Input/Output
Print
While loops
If/Else statements

"""


# GUESS THE NUMBER
from random import randint

# score = 0
# score2 = 0
# play = int(input("How many times do you want to play this game? "))
X = randint(1,100)  
# print(X)

# for i in range(1,play):
Y = int(input("Guess a number between 0 and 100: "))
if (X == Y):
    # score = score + 1 
    print("You guess the right number, which is", X)
elif (Y > X):
        print("Wrong! The number is too high. The correct answer is", X)
else:
    print("Wrong! The number is too low. The correct answer is", X)

    
    
     

