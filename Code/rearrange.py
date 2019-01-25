import random
import sys

def rearrange():
    new_word_set = sys.argv[1:]
    random.shuffle(new_word_set)
    print(new_word_set)

rearrange()
