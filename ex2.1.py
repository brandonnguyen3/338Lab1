#The error with this code is in line 12. The print statement has an illegal character: backtick, instead of a single quote.
#The program checks if the number entered in the command line is a prime number or not. 
# Prints "Yes" if it´s a prime number, "No" if it's not

import sys
def do_stuff():
    number = int(sys.argv[1])
    if number < 2:
        print('No')
    else:
        for i in range(2, number):
            if number % i == 0:
                print('No')
                return
        print('Yes') #fix the error here
          
# Test the function
do_stuff()