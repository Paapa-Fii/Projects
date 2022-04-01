# DICE ROLLING STIMULATOR

"""
 Dice Rolling Simulator

The Goal: Like the title suggests, this project involves writing a program that simulates rolling dice. When the program runs, it will 
randomly choose a number between 1 and 6. (Or whatever other integer you prefer — the number of sides on the die is up to you.) The 
program will print what that number is. It should then ask you if you’d like to roll again. For this project, you’ll need to set the min 
and max number that your dice can produce. For the average die, that means a minimum of 1 and a maximum of 6. You’ll also want a function 
that randomly grabs a number within that range and prints it.
Concepts to keep in mind:

Random
Integer
Print
While Loops
"""

#  This is a simple roll a dice task using random, integer, print \
# and for loop

import random                                     #this is a library containing many functions

def roll_dice(rolls):                            #this is a function called roll_dice and indicated by def
    for i in range(0,rolls):
        number = random.randint(1,6)             #gives random numbers from 1 to 6
        print("---")
        print('-' + str(number) + '-')
        print("---")
        print()
    menu()



def menu():                                         #this is another function for a menu
    print("1. Roll a dice")
    print("2. Roll a dice multiple times")
    print("3. Exist program")
    print()
    choice = int(input("Enter your choice here: "))
    print()
    print("--------------------------------")
    if (choice == 1):
        roll_dice(1)

    if (choice == 2):
        rolls = int(input('How many times do you want to roll the dice: '))
        roll_dice(rolls)
    print("--------------------------------")
    if (choice == 3):
        quit()

    

menu()

