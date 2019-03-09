"""
Jake Shams helped me to understand and build markov chain - he worked with me and gave permission to use his code. 
"""

import cleaner
from cleaner import file_cleaner
from linkedlist import LinkedList
from dictogram import Dictogram
import random

class Second_Order_Markov_Chain(Dictogram):
    '''Building Secon Order Markov chain '''

    def __init__(self, word_list=None):
        super(Second_Order_Markov_Chain, self).__init__()
        self.word_list = word_list
        self.length = 0
        if self.word_list is not None:
            self.create(self.word_list)

    def create(self, word_list):
        for i, first_word in enumerate(word_list):
            if first_word == word_list[-2]:
                return
            second_word = word_list[i + 1]
            word_pair = "{} {}".format(first_word, second_word)
            # print(word_pair[2])
            third_word = word_list[i + 2]
            self.add_to_self(word_pair, third_word)

    def add_to_self(self, word_pair, next_word):
        if word_pair in self:
            self[word_pair].add_count(next_word)
        else:
            self[word_pair] = {next_word: 1}
            self.length += 1

    def random_sentence(self, sentence_length):
        if sentence_length <= 0:
            return
        elif sentence_length == 1:
            return random.choice(self.word_list)
        sentence = []
        random_num_from_zero_length = random.randint(0, self.length)

        i = 0
        for key in self:
        
            if random_num_from_zero_length == 0:
                key_as_list = key.split(" ")
                sentence.extend(key_as_list)
                break
            if i == random_num_from_zero_length - 1:
                key_as_list = key.split(" ")
                sentence.extend(key_as_list)
                break
            i += 1
        x = 2
        while x < sentence_length:
  
            word_pair = "{} {}".format(sentence[-2], sentence[-1])
            new_word = self.random_next_word(word_pair)
            if new_word:
                sentence.append(self.random_next_word(word_pair))
            else:
                random_num_from_zero_length = random.randint(0, self.length)
                i = 0
                for key in self:
                    if i == random_num_from_zero_length:
                        key_as_list = key.split(" ")
                        sentence.extend(key_as_list)
                        break
            x += 1
        return " ".join(sentence)

    def random_next_word(self, word_pair):
        if word_pair not in self:
            return False
        rand_prob_dist = []
        total_tokens = 0
        for key in self[word_pair]:
            total_tokens += self[word_pair][key]
        incrementor = 0
        for key in self[word_pair]:
            prob_value = float(self[word_pair][key]) / \
                float(total_tokens) + incrementor
            incrementor = prob_value
            rand_prob_dist.append((key, prob_value))
        rando_num = random.random()
        for i in rand_prob_dist:
            if i[1] > rando_num:
                return i[0]


if __name__ == '__main__':
    txt = file_cleaner(cleaner.file)
    m_chain = Second_Order_Markov_Chain(txt)
    random_text = m_chain.random_sentence(10)