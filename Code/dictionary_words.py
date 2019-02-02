import random
import sys
from datetime import datetime


def read_doc():
    sample = ''
    word_num = int(sys.argv[1])
    the_file = open('/usr/share/dict/words', 'r')
  
    for line in the_file:
        sample += str(line)
    listed_sample = sample.split()
    print(' '.join(random.choices(listed_sample, k=word_num)))

read_doc()

# show execution time
start_time = datetime.now()
print(datetime.now()-start_time)
