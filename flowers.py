"""
JT Vannoy, 28 Feb 2018
Draws randomized flowers on click

"""

import turtle
import random


def bloom(tortoise, fcolor, length, num_petals):
    tortoise.pencolor('red')  # pencolor set red and shape is filled
    tortoise.fillcolor(fcolor)
    tortoise.begin_fill()
    num_deg = 1080 / num_petals  # degrees scaled to num_petals 
    for segment in range(num_petals):  # loop scales to num_petals
        tortoise.forward(length)
        tortoise.left(num_deg)
    tortoise.end_fill()


def stem(tortoise, length, colors):
    tortoise.pencolor(colors)  # stem color randomized 
    tortoise.pensize(length / 20)  # stem adjusts to flower size
    tortoise.up()
    tortoise.forward(length / 2)
    tortoise.down()  # draw stem
    tortoise.right(90)
    tortoise.forward(length)


def flower(tortoise, fcolor, length, num_petals, colors):
    # all functions for making flower called
    bloom(tortoise, fcolor, length, num_petals)
    stem(tortoise, length, colors)


def grow_flower(x, y):
    # span range modified to better fit screen
    span = random.randrange(20, 180)
    # colors for flower
    fill = random.choice(['yellow',
    'pink', 'red', 'purple', 'brown', 'orange'])
    num_petals = random.choice([5, 7, 10, 20])  # petals randomized
    colors = random.choice(['green', 'brown',
    'pink', 'black'])   # stem color randomized
    # lines below reorient turtle 
    tortoise = turtle.Turtle()
    tortoise.hideturtle()
    tortoise.speed(6)
    tortoise.up()
    tortoise.goto(x, y)
    tortoise.setheading(0)
    tortoise.pensize(1)
    tortoise.down()
    flower(tortoise, fill, span, num_petals, colors)  # flower() is called


george = turtle.Turtle()
george.hideturtle()
screen = george.getscreen()
screen.onclick(grow_flower)
screen.mainloop()
