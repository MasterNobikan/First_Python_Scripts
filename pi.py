'''Monte Carlo Pi
JT Vannoy -- Mar 17, 2018
'''

from random import *
from math import *



def monte(darts):
# ratio = pi/4 so pi approx 4*fraction

    count = 0
    no = 0
    approx = 0
    for i in range(darts): 
        x = random()
        y = random()
        count = sqrt((x**2) + (y**2))
        if count <= 1:  # check to see if (x,y) in circle
            approx = approx + 1 
        else:
            no = no + 1
    return (approx/darts)*4  # return approximate pi 

def main():
    print('Monte Carlo Simulator for Approximating PI\n')
    
    # ask user for range and terms
    choice = int(input('How many darts do you want to throw: '))

    print('The approximated value of pi is {}.'.format(str(monte(choice))))



main()
