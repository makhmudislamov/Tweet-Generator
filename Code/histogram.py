from datetime import datetime
import sys


# Input file name as string
# Output list of words as [string]
def get_corpus(file):
    # source_text = open(file, 'r')
        # for line in source_text:
    #     hist_string += str(line).lower()
    # wordlist = hist_string.split()
    with open(file) as f:
        text = f.read()
        # print('TEXT: {}'.format(text))
        words_list = text.lower().split(' ')
        # print('words_list: {}'.format(words_list))
        return words_list



def histogram(file):
    """
    This function returns histogram as dictionary, 
    list of list or list of tuples depending on user's choice.
    """
    word_freq = []
    # hist_string = ''

    # Input file name as string
    # Output list of words as [string]
    word_list = get_corpus(file)
    sorted_word_list = sorted(word_list)
    print(sorted_word_list)

    counter = 1

    for left_index in range(0, len(sorted_word_list)-1):
    #     # issue is here , dont use .count >> inefficient
        # for right_index in range((left_index +1), len(sorted_word_list)):
        #     if (sorted_word_list[left_index] == sorted_word_list[right_index]):
        #         counter += 1
        #         # word_freq.append(counter)
        #         print('COUNTER: {}'.format(counter))
        #     elif (sorted_word_list[left_index] != sorted_word_list[right_index]):
        #         word_freq.append(counter)
        #         counter = 1
        if sorted_word_list[left_index] == sorted_word_list[left_index+1]:
            counter += 1
            print('COUNTER: {}'.format(counter))
        else:
            counter = 1
        print(left_index)
    print(len(sorted_word_list))
    print(word_freq)
                
    # print(word_freq)

    #     word_freq.append(word_list.count(word))
    #     # bugfix this and print
    #     # list_of_list.append([wordlist, histogram]))

    # # zipping wordlist and histogram
    # zipped_histogram = zip(word_list, word_freq)
    
    # if output_choice == 'tuple':
    # # # printing dictionary, key-value pair >> uncomment the line below
    #     print(list(zipped_histogram))
    # # elif output_choice == 'llist':
    # #     print()
    # elif output_choice == 'dict':
    # # # printing list of tuple >> uncomment the line below
    #     print(dict(zipped_histogram))
    # print(word_freq)

    # print(dict(zipped_histogram))
    
    
if __name__ == "__main__":
    # output_choice = str(sys.argv[1])
    # histogram()
    # start_time = datetime.now()
    # print(datetime.now()-start_time)
    file = 'sample_words.txt'
    histogram(file)
   

# def unique_words():
#     ...

# def frequency():
#     ...

# TODO 1>> printing list of lists
# TODO 2>> cleaning up the file from punctuations
# TODO 3>> def unique words
# TODO 4>> def frequency
