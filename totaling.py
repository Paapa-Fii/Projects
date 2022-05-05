# TOTALING A LIST

# This program get integers from the user and
# calculates the total of the values in a list

def main():

    # Create an empty list
    numbers = []

    # Create a variable to control the loop
    again = 'y'

    # Create a while loop to get all the numbers
    while again == 'y':
        
        # Get numbers from user.
        num = int(input('Enter a number: '))
        print()

        # Append the list
        numbers.append(num)

        # Ask the user whether there is more input
        print('Do you want to enter another number, '
        'y = yes and n = no')
        again = input()
        print()

    # Display the list
    print('Here are the numbers you entered: ')
    print(numbers)
    print()

    # Create a variable to use an accumulator.
    total = 0

    # Calculate the total of the elements.
    for value in numbers:
        total += value
    
    # Display the total of the list elements.
    print('The total of the elements is', total)

# Call the main function
main()
