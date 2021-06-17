import random

def main():
    #print progrm name
    print()
    print("Rock, Paper, Scissors!!")
    print("with HAL")

    game_over = False

    while not game_over:
        c = random.choice(['r','p','s'])
        p = input('Rock (r), Paper(p), Scissors(s): ')

        print()
        print('You selected', p, 'and I selected', c)
        print()
        
        if c == p:
            print('We Tie!, Again!')
        elif c == 'r' and p == 'p':
            print('Rats! You win..')
            game_over = True
        elif c == 'p' and p == 'r':
            print('Ha, I beat you puny human!!')
            game_over = True
        elif c == 'r' and p == 's':
            print('Ha, I beat you puny human!!')
            game_over = True
        elif c == 's' and p == 'r':
            print('Rats! You win..')
            game_over = True
        elif c == 'p' and p == 's':
            print('Rats! You win..')
            game_over = True
        elif c == 's' and p == 'p':
            print('Ha, I beat you puny human!!')
            game_over = True
            

main()
