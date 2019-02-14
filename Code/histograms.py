from cleaner import file_cleaner
import cleaner
import random
import sys


def histogram_dict(word_list):
    """
    Input >>> array of strings
    Output >>> histogram in a dictionary format
    """
    hist_dict = {}

    for word in word_list:
        if word not in hist_dict:
            hist_dict[word] = 1
        else:
            hist_dict[word] += 1

    return hist_dict
    # print(hist_dict)
    
def histogram_tuple(word_list):
    """
    Input >>> array of strings
    Output >>> histogram in a tuple format
    """
    hist_tuple = []
    #TODO: adding extra word for first value  -FIX IT
    hist_tuple.append((word_list[0], 1))
    for word in word_list:
        found = False
        for index, value in enumerate(hist_tuple):
            if value[0] == word:                              
                found = True
                num = value[1] + 1
                hist_tuple.pop(index)                         
                hist_tuple.append((word, num))       
                break
        if not found:
            hist_tuple.append((word, 1))

    # print(hist_tuple)
    return hist_tuple


def histogram_list(word_list):
    """
    Input >>> array of strings
    Output >>> histogram in a list of list format
    """
    hist_list = []

    for word in word_list:
        found = False                       
        for value in hist_list:
            if word in value[0]:
                found = True
                value[1] += 1

        if not found:
            hist_list.append([word, 1])

    return hist_list 
    # print(hist_list)

def format_choice(cl_input):
    """
    This is a helper function. A user can choose an output format
    """
    if cl_input == 'list':
        histogram_list(file_cleaner(cleaner.file))
    elif cl_input == 'tuple':
        histogram_tuple(file_cleaner(cleaner.file))
    elif cl_input == 'dict':
        histogram_dict(file_cleaner(cleaner.file))


if __name__ == '__main__':
    # cl_input = str(sys.argv[1])
    # format_choice(cl_input)
    print(histogram_tuple(file_cleaner(cleaner.file)))
