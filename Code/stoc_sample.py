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
    

def stochastic_sample(histogram):
    """
    Returns random word from the dictionary based on frequency.
    """
    tokens = 0

    cumulative_probability = 0.0
    # you can use sum()
    for word_frequency in histogram.values():
        tokens += word_frequency # this works until here, tested with print
    
    random_choice = random.uniform(0, 1)
    for word, word_frequency in histogram.items():
        cumulative_probability += word_frequency/tokens
        if cumulative_probability >= random_choice:
            return word
            
    
def test_iteration(histogram, iteration):
    """
    Creates hisogram based on stochastic sampling and iterating given amount to prove stochastic sampmling
    """
    word_list = [stochastic_sample(histogram) for x in range(iteration)]
    return histogram_dict(word_list)
   



if __name__ == "__main__":
    start_time = datetime.now()
    # input_words = list(sys.argv[1:])
    # rand_word()
    histogram = {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1}
    print(test_iteration(histogram, 10000))  
    print(datetime.now()-start_time)



