import histogram
import sys
from random import randint

# command line input >> file name
cl_input = str(sys.argv[1])
def rand_word(histogram):
    """
    This function returns a random word from the histogram
    """
    file = open(cl_input, 'r')
    
