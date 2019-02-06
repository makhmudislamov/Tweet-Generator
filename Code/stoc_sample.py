import random
from histograms import *
# import sys
from datetime import datetime

def rand_word():
    """
    Input >>> string array from CL
    Output >>> random string from array
    """
    rand_index = random.randint(0, len(input_words)-1)
    word = input_words[rand_index]
    print(word)


def rand_hist_word():
    """
    This function creates dictionary from CL words.
    Then prints random word from the dictionary
    """
    histogram = histogram_dict(input_words)
    rand_key = random.randint(0, len(histogram)-1)
    print(histogram)
    print([key for key in histogram.keys()][rand_key])
    



if __name__ == "__main__":
    start_time = datetime.now()
    input_words = list(sys.argv[1:])
    # rand_word()
    rand_hist_word()
    print(datetime.now()-start_time)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# import histogram_draft
# import sys
# import random


# def rand_word(histogram):
#     """
#     This function returns a random word from the histogram
#     """
#     source_file = open(cl_input, 'r')
#     for key in source_file:
#         print(key)



# if __name__ == "__main__":
#     # command line input >> file name
#     cl_input = str(sys.argv[1])
#     rand_word(histogram_draft)
    
# # How to print dictionary:
# # source_file = {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1}
# #     for key in source_file:
# #         print(key)



