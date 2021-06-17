'''
Demo Problem March 5
'''


def sing_verse(current_bottle, drink):
    # prints the general verse form
    print(current_bottle, 'bottles of', drink,'on the wall')
    print(current_bottle, 'bottles of', drink)
    print('Take one down, pass it around')
    print(current_bottle -1, 'bottles of', drink)


def sing_song(start_bottles, drink):
    for bottle in range(start_bottles,0,-1):
        sing_verse(bottle, drink)
        print(end='\n')


def main():
    total_bottles = int(input('How many bottles: '))
    drink_choice = input('What drink?: ')
    sing_song(total_bottles, drink_choice)


main()
