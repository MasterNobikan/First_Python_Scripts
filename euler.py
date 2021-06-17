'''JT Vannoy
8 March, 2018
calculates an approximate value of e
'''

import math

def factorial(n):  # the function calculates factorial
    nint = 1
    for i in range(1,n+1):
        nint = nint * i
    return nint

def e(n):  # this function calculates e, using factorial to change denominators
    eulers = 1
    for v in range(1,n):
        eulers = eulers + (1/factorial(v))
    return eulers
    

def main():  # main prints welcome, gets number of steps to use, and prints the final result
    print()
    print('The e Approximation Program\n')
    entry = int(input('How many terms do you want to use for the approximation: '))
    print()
    print('The approximated value of e is {}, which has an error of {} .'
          .format(e(entry),(math.fabs(math.e-e(entry)))))
    
    
main()
