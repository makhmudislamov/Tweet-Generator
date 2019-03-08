import random
from dictogram import Dictogram
from linkedlist import LinkedList

fish = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']

class Markov_Chain(Dictogram):
    """Creates first order markov chain"""
    def __init__(self, word_list = None):
        super(Markov_Chain, self).__init__()
        self.word_list = word_list
        if self.word_list != None:
            self.create(self.word_list)


    def create(self, word_list):
        for i, word in enumerate(word_list):
            if i == len(word_list):
                return self
                # is a word in the chain?
            if word in self:
                # is the following word in the chain
                word.add_count(word_list[i+1], 1)
            else:
                self[word] = {word_list[i+1]: 1}


''' print Tests '''
fish = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
my_chain = Markov_Chain(fish)
print(my_chain)



# if __name__ == '__main__':
#     pass

