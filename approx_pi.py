'''use following series: pi = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - ...
'''

def approx_pi(terms):
    sum_of_terms = 0
    multiplier = 1
    # terms * 2 because of odd number sequence
    for i in range(1, terms*2, 2):
        sum_of_terms = sum_of_terms + (4/i * multiplier)
        multiplier = multiplier * -1
    return sum_of_terms
    
def main():
    # asks for number of terms 
    steps = int(input('How many terms: '))

    # displays the result
    print('Your estimated value of pi is', approx_pi(steps))

main()
    
    
