from datetime import datetime
import sys

output_choice = str(sys.argv[1])
def histogram():
    
    word_freq = []
    hist_string = ''
    source_text = open('sample_words.txt', 'r')
    for line in source_text:
        hist_string += str(line).lower()
        
    wordlist = hist_string.split()

    # iterate over the text
    # keep record of each word >> how many times the word is repeated
    # append histogram as key-value pair
    # print the histogram
    for word in wordlist:
        # issue is here , dont user .count >> inefficient
        word_freq.append(wordlist.count(word))
        # bugfix this and print
        # list_of_list.append([wordlist, histogram]))

    # zipping wordlist and histogram
    zipped_data = zip(wordlist, word_freq)
    

    if output_choice == 'dict':
    # # printing dictionary, key-value pair >> uncomment the line below
        print(dict(zipped_data))
    elif output_choice == 'tuple':
    # # printing list of tuple >> uncomment the line below
        print(list(zipped_data))

    print(word_freq)
    
    

histogram()
start_time = datetime.now()
print(datetime.now()-start_time)

# def unique_words():
#     ...

# def frequency():
#     ...
