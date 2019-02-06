import random
import sys
from datetime import datetime



result_arr = []

def random_words(word):
    """
    This function rearranges the order of user input strings.
    """
    rand_index = random.randint(0, len(input_words)-1)
    word = input_words[rand_index]
    
    return word

if __name__ == "__main__":
    start_time = datetime.now()
    input_words = list(sys.argv[1:])
    print(' '.join(map(random_words, input_words)))
    print(datetime.now()-start_time)
    
