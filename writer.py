
def main():
    file_name = input('Where would you like to save your data? ')

    print()

    new_file = open(file_name, 'w')

    text = input('Enter a line of data: ')
    while text != 'exit':
        new_file.write(text + '\n')
        text = input('Enter a line of data: ')

    new_file.close()


main()
