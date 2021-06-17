"""
Class
and dice demo
"""

from random import *


class MSDie:
    def __init__(self, sides): # constructor
        # known about self
        self.sides = sides
        self.value = 1

    def get_value(self):
        return self.value

    def get_sides(self):
        return self.sides

    def roll(self):
        self.value = randint(1, self.sides)

    def super_mega_roll(self):
        for i in range(100):
            self.value = randint(1,self.sides)


def main():
    # make new die
    d1 = MSDie(6)
    d2 = MSDie(2)
    d1.roll() # updating method so no set new value
    d2.super_mega_roll()
    print(d1.get_value()) # gives value
    print(d2) # shows place in memory

main()
