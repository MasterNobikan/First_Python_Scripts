"""Pig Latin Converter
problem taken from textbook
"""


def username(first, last):
    return "{}_{}".format(last, first[:1])

def piglatin(word):
    return '{}{}ay'.format(word[1:], word[:1])

def main():
    word = input('What word do you want to convert:')
    first = input('First name: ')
    last = input('Last name: ')
    print(username(first, last))
    print(piglatin(word))

main()
