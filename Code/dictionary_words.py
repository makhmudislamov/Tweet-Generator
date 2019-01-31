import random
import sys

def read_doc():
    sample = ''
    # word_num = int(sys.argv[1:])
    f = open('sample_words.txt', 'r')
    # loop thourhg the lines of doc
    # print random x amount of words from the list
    # x amount = user input number

    for line in f:
        sample += str(line)
    print(sample)

read_doc()


# str = 'book pen paper pencil'
# x = str.split()
# print(x)
# y = len(x)

# z = random.randrange(-1, y)
# print(x[z])
