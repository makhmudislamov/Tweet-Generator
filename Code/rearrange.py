import random
import sys
from datetime import datetime


# def rearrange():
#     new_word_set = sys.argv[1:]
#     random.shuffle(new_word_set)
#     print(new_word_set)

# rearrange()


start_time = datetime.now()

input_words = list(sys.argv[1:])
result_arr = []
dup_words = set()
def random_words(word):
    rand_index = random.randint(0, len(input_words)-1)
    word = input_words[rand_index]
    
    return word

    # create new array result_arr = []
   
    # loop through input_words
    # for word in input_words:
    #     if word not in dup_words:
    #     # if word not in result_arr:
    #         result_arr.append(word)
    #         dup_words.add(word)
    # return result_arr


print(' '.join(map(random_words, input_words)))

# print(result_arr)
print(datetime.now()-start_time)

