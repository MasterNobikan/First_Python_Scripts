'''
The program below encrypts and decrypts txt
files with a Caesar cipher
JT Vannoy, 29 March, 2018
'''


def encrypt(message, key, mode):
    e_message = ''
    d_message = ''
    if mode == 'e':
        for i in message:
            e_message = e_message + chr((ord(i)+key))
        return e_message
    elif mode == 'd':
        for i in message:
            d_message = d_message + chr((ord(i)-key))
        return d_message


def main():
    print('The Caesar Cipher Program')
    file_start = str(input('Enter the name of a file: '))
    key = int(input('Enter a key value: '))
    mode = str(input('Do you want to (e)ncrypt or (d)ecrypt?'))

    new_file = open(file_start, 'r') # open original file
    file_text = new_file.read()
    new_file.close()

    # processes file name for later printing
    if mode == 'e':
        file_name = '{}_encrypted.txt'.format(file_start[:file_start.find('.')])
    elif mode == 'd':
        file_name = '{}_decrypted.txt'.format(file_start[:file_start.find('.')])

    new_e = encrypt(file_text, key, mode)  # string from encrypt
    new_output = open(file_name, 'w')
    new_output.write(new_e)  # writing to new file
    new_output.close()

    if mode == 'e':
        print('Encrypting...\n')
        print('Your file has been encrypted to', file_name)

    elif mode == 'd':
        print('Decrypting...\n')
        print('Your file has been decrypted to', file_name)


main()
