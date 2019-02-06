import histogram
import sys
import random


def rand_word():
    """
    This function returns a random word from the histogram
    """
    source_file = open(cl_input, 'r')
    for key in source_file:
        print(key)




if __name__ == "__main__":
    # command line input >> file name
    cl_input = str(sys.argv[1])
    rand_word()
# How to print dictionary:
# source_file = {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1}
#     for key in source_file:
#         print(key)
