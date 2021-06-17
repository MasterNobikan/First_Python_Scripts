import math

def improved_adder(x,y):

    if not isinstance(x,int) or not isinstance(y,int):
        return None
    elif x<0 or y<0:
        return None
        
    return x + y


def improved_multiplier(x,y):
    return x * y


def main():
    print('This is my math code that is better than Python\'s')
    x = 4
    y = 6
    print(improved_adder(x,y))
    print(improved_multiplier(x,y))
    print(math.__name__)

if '__name__' == '__main__':  # only runs main when run directly
    main()
