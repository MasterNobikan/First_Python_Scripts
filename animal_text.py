def roar(n):
    return 'r' + ('o' * n) + 'r!'


def speak(animal):
    if animal == 'cat':
        word = 'meow.'
    else:
        word = roar(10)

    print('The', animal, 'says', word)


speak('monkey')
