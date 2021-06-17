
# open file and read contents
my_file = open('message.txt', 'r')
text = my_file.read()

text = text.replace('\n', ' ')
text = text.replace('  ', ' ')

words = text.split(' ')

d = {}
for word in words:  # place in dictionary
    d[word] = 0

for word in words:  # count the repeat words
    d[word] = d[word] + 1

# now sort
d_list = list(d.keys())
d_list.sort()

for word in d_list:
    print(word, ' = ', d[word])


# close file
my_file.close()
