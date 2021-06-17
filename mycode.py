"""
original for file test_mycode
"""

def factorial(number):
    if isinstance(number, int) and number >= 0:
        f = 1
        for i in range(1,number+1):
            f = f * i
        return f
    else:
        return None


def adder(num1, num2):
    return num1 + num2


def main():
    print(factorial('hello'))


if '__name__' == '__main__':
    main()
