"""
this is the bug testing for mycode
use as example and reference
"""

from mycode import *

def test_factorial():

    assert factorial(0) == 1, 'Failed factor(0) test'
    assert factorial(1) == 1, 'Failed factorial(1) test'
    assert factorial(3) == 6, 'Failed factorial(3) test'
    assert factorial(4) == 24, 'Failed factorial(4) test'
    assert factorial(-1) == None, 'Failed -1 test'
    assert factorial(-7) == None, 'Failed -7 test'
    assert factorial('python') == None, 'Failed string test'
    
    print('Passed all tests of factorial!')


def test_adder():

    assert adder(3,5) == 8, 'Failed test(3,5)'
    assert adder(-3,-5) == -8, 'Failed negatives test'
    
    print('passed all tests of adder!')


def test():
    # run all tests
    test_factorial()
    test_adder()

test()
