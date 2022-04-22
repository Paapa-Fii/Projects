# First Attempt 

# This program is used to calculate the gross pay
# of employees of the neigborhood coffee shop


hr_pay_rate = 20

def main():
    #create an empty list to hold names and pay
    name_list = []

    # variable to control loop
    again = 'y' 

    # Add some names to the list
    while again == 'y':

        # Get a name from the user.
        name = input('Enter name of employee: ')

        # Get number of hours of worked by employee
        number_hr = eval(input('Enter number of hours worked by employee: '))

        # formula for calculating gross pay of each employee
        gross_pay = hr_pay_rate * number_hr

        print()

        #put the name and gross pay together
        employee = name, gross_pay
        print(employee)
        print()

        #append list
        name_list.append(employee)

        # Add another one?
        print('Do you want to add another name?')    
        again = input('y=yes, anything else = no: ')
        print()

    # Display the names that were entered.
    print('Here are the names and gross pay of the employees you entered.')    
    for employee in name_list:
        print(employee)

#call the function
main()


  

    
