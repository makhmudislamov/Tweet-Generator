import random
import sys
from datetime import datetime


input_words = list(sys.argv[1:])
result_arr = []

def random_words(word):
    """
    This function rearranges the order of user input strings.
    """
    rand_index = random.randint(0, len(input_words)-1)
    word = input_words[rand_index]
    
    return word
# Mapping and outputtin in terminal. 
print(' '.join(map(random_words, input_words)))

start_time = datetime.now()
print(datetime.now()-start_time)

