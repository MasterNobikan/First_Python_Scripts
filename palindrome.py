
"""finds if string is the same reversed or not"""


def is_palindrome1(some_string):
    left = 0
    right = len(some_string) - 1
    while left < right:
        if some_string[left] == some_string[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


def is_palindrome(s):
    return s == s[::-1]


def main():
    s = input('Enter a string: ')

    # print result
    if is_palindrome(s):  # is True
        print('The string is a palindrome.')
    else:
        print('The string is not a palindrome.')


main()