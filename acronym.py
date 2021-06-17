"""
The program takes a string and creates an acronym
JT Vannoy
12 April, 2018
"""


def acronym(phrase):  # returns an acronym of the string
    shortened = ""
    words = phrase.split()
    for part in words:
        shortened = shortened + part[0]  # connect first letter of words
    return shortened.upper()


def largest(phrase):  # largest finds the longest word in string
    biggest = ""
    words = phrase.split()  # creates a list
    for part in words:
        if len(part) > len(biggest):
            biggest = part  # sets larger len to biggest
        return biggest


def main():
    print('The Acronym Program\n')
    the_phrase = input('Please enter a phrase: ')  # asks user for string
    while the_phrase != 'quit':
        print('The acronym is {}, and the largest word is {}.\n'.format(acronym(the_phrase),
                largest(the_phrase)))  # print out final message
        the_phrase = input('Please enter a phrase: ')  # ask question again
    print('Thanks for using this program!')  # quit message


main()
