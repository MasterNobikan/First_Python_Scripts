

def find_all(string_to_search, char):
    list_of_positions = []
    loc = string_to_search.find(char)
    while loc != -1:
        list_of_positions.append(loc)
        loc = string_to_search.find(char, loc + 1)


    return list_of_positions


def main():
    string = 'A Lannister always pays his debts.'
    character = 'a'

    result = find_all(string, character)

    if len(result) == 0:
        print('No characters found.')
    else:
        print('Characters found at following positions: ', result)


main()
