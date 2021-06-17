from math import *

def main():
    # get inout from user
    a = float(input("enter side 1: "))
    b = float(input("enter side 2: "))
    c = float(input("enter side 3: "))

    # compute answer
    s = (a + b + c) / 2
    area = sqrt(s * (s-a) * (s-b) * (s-c))

    #display answer
    print("The area of the triangle is", area, end=" because im batman\n")
    print("Thanks for using my program")

main()
    

        
