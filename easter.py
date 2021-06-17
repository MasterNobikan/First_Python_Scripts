"""Program from class computes the date of Easter
 years 1954, 1981, 2049, 2076 are adjusted
"""


def compute_easter(year):
    # compute needed values
    a = (year % 19)
    b = (year % 4)
    c = (year % 7)
    d = ((19*a + 24) % 30)
    e = ((2*b + 4*c + 6*d + 5) % 7)

    day = 22 + d + e

    # check choice is an 'except' year
    if year in [1954, 1981, 2049, 2076]:
        day = day - 7
    
    if day > 31:
        return  str(day - 31) + ' April'  # str + str only
    else:
        return str(day) + ' March'


def main():
    year = int(input('enter a year (1900-2099): '))
    if 1900 <= year <= 2099:
        print('Easter will be on', compute_easter(year),
              'in', year)
    else:
        print('Error: Value not in range. Exiting progrm')


main()
