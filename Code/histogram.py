from datetime import datetime

def histogram():
    histogram = []
    hist_string = ''
    source_text = open('the_matrix.txt', 'r')
    for line in source_text:
        hist_string += str(line)
    wordlist = hist_string.split()

    # iterate over the text
    # keep record of each word >> how many times the word is repeated
    # append histogram as key-value pair
    # print the histogram
    for word in wordlist:
        histogram.append(wordlist.count(word))

    zipped_data = zip(wordlist, histogram)

    # print("Frequencies\n" + str(histogram) + "\n")
    print(list(zipped_data))

histogram()
start_time = datetime.now()
print(datetime.now()-start_time)

# def unique_words():
#     ...

# def frequency():
#     ...
