import random
import sys

def read_doc():
    sample = []
    # word_num = int(sys.argv[1:])
    f = open('sample_words.txt', 'r')
    # loop thourhg the lines of doc
    # print random x amount of words from the list
    # x amount = user input number

    for line in f:
        sample.append(line)
    print(sample)

read_doc()
