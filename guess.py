import random

the_number = random.randrange(1,11)


def main():
    # initialize variable for end
    win = False  
    # print intro
    print("Guessing Game 9000\n")
    for i in range(3):  # loop for guesses
        guess = int(input("What is my number?\n"))
        if guess == the_number:
            print()
            print("G00d J0b!")
            win = True
            break  # stops loop if correct
        else:
            if guess < the_number:
                print()
                print("nO!, Too low")
            else:
                print("n0!, Too High")
            
    if win == True:
        print("You da Baws!!")
    else:
        print("\nThank you for playing!")  # end message


main()

