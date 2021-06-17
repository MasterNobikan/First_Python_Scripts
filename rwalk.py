'''
rwalk.py
Visually displays a random turtle walk
NOTE this is random_walk book example
'''

import turtle
import random
import math

def random_walk(steps, tortoise, draw):
    x = 0
    y = 0
    move_length = 10
    if draw == False or True:
        for step in range(steps):
            r = random.random()
            if r < 0.25:
                x = x+1
            elif r < 0.5:
                y = y + 1
            elif r < 0.75:
                x = x - 1
            else:
                y = y - 1
    # comment line below out for monte_carlo 
        #tortoise.goto(x * move_length, y * move_length)
    return math.sqrt(x*x + y*y)
    

def rw_monte_carlo(steps, trials):
    total_dist = 0
    for trial in range(trials):
        distance = random_walk(steps, None, False)
        total_dist = total_dist + distance
    return total_dist / trials


def main():
    walks = int(input("How many steps of random do you want?\n"))
    jy = turtle.Turtle()
    random_walk(walks, jy, True)
    jy.hideturtle()
    print("the distance from the start:", random_walk(walks, jy, True))


print(rw_monte_carlo(500,5))
print(rw_monte_carlo(1000,5))

