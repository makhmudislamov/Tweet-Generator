from datetime import datetime
import sys

output_choice = str(sys.argv[1])
def histogram():
    """
    This function returns histogram as dictionary, 
    list of list or list of tuples depending on user's choice.
    """
    word_freq = []
    hist_string = ''
    source_text = open('sample_words.txt', 'r')

    for line in source_text:
        hist_string += str(line).lower()
        
    wordlist = hist_string.split()

    for word in wordlist:
        # issue is here , dont use .count >> inefficient
        word_freq.append(wordlist.count(word))
        # bugfix this and print
        # list_of_list.append([wordlist, histogram]))

    # zipping wordlist and histogram
    zipped_histogram = zip(wordlist, word_freq)
    
    if output_choice == 'dict':
    # # printing dictionary, key-value pair >> uncomment the line below
        print(dict(zipped_histogram))
    elif output_choice == 'tuple':
    # # printing list of tuple >> uncomment the line below
        print(list(zipped_histogram))

    print(word_freq)
    
    

histogram()
start_time = datetime.now()
print(datetime.now()-start_time)

# def unique_words():
#     ...

# def frequency():
#     ...
