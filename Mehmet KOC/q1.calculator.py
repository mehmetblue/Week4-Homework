"""
1) Calculator:

General Information:
I want to use a program which can calculate basic mathematical operations.

Acceptance Criteria:
* The calculator must support the Addition, Subtraction, Multiplication and Division operations.
* All operations must be in a different module as method. 
* Operations must define with two float numbers as parametres. 
* Use math.ceil() for all results. 
* Create a menu to choose an operation. 
* User can choose invalid options, so you must handle all possible error. (Use try except :))
* Inform user what type of error occured (TypError, ValueError etc.)
* This process must continue until user want to quit from calculator.

"""

from math import ceil
import sys

from add import add
from subtract import subtract
from multiply import multiply
from divide import divide


print("Select the operation: ")
print("a --> Add")
print("s --> Subtract")
print("m --> Multiply")
print("d --> Divide")


while True:

    try:

        # taking inputs from the user
        choice = input("Please type your choice('a'/'s'/'m'/'d'): ")
            

        # checking if the choice is correct and operaterates
        if choice in ('a', 's', 'm', 'd'):
            n1 = float(input("Please type the first number: "))
            n2 = float(input("Please type the second number: "))

            if choice == 'a':
                print(n1, "+", n2, "=", ceil(add(n1, n2)))

            elif choice == 's':
                print(n1, "-", n2, "=", ceil(subtract(n1, n2)))

            elif choice == 'm':
                print(n1, "*", n2, "=", ceil(multiply(n1, n2)))

            elif choice == 'd':
                print(n1, "/", n2, "=", ceil(divide(n1, n2)))
            
            # check if user wants another calculation
            # break the while loop if answer is "n" (no)
            next_calculation = input("Do you want to continue? (y/n): ")
            if next_calculation == "n":
                break
        
        # if the choise is not correct, show the warning message
        else:
            print("Please type the one of the correct options!")
    
    # showing type of error
    except:

        print("Oops", end=" - ")
        #print(sys.exc_info()[0])
        
        msg=str(sys.exc_info()[0])

        print(msg.split("'")[1])