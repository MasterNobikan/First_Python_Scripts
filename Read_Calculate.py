
def main():
    # establish connections to IO files
    input_file = open('test2.txt', 'r')
    output_file = open('output2.txt', 'w')

    # initialize variables
    average = 0
    count = 0

    # compute average
    for line in input_file:
        # int ignores whitespace and \n's
        average = average + int(line)
        count = count + 1
    average = average / count

    # save average to file
    output_file.write(str(average))

    input_file.close()
    output_file.close()
    

main()
