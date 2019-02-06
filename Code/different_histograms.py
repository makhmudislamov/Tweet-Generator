import file_cleaner

word_list = ['one', 'fish', 'two', 'two', 'fish', 'red', 'fish', 'blue', 'fish']

def histogram_dict(word_list):
    """
    Input >>> array of strings
    Output >>> histogram in a dictionary format
    """
    hist_dict = {}

    for word in word_list:
        if word not in hist_dict:
            hist_dict[word] = 1
        else:
            hist_dict[word] += 1

    print(hist_dict)

def histogram_tuple(word_list):
    """
    Input >>> array of strings
    Output >>> histogram in a tuple format
    """
    hist_tuple = []

    hist_tuple.append((word_list[0], 1))
    for word in word_list:
        found = False
        for index, value in enumerate(hist_tuple):
            if value[0] == word:                              
                found = True
                num = value[1] + 1
                hist_tuple.pop(index)                         
                hist_tuple.append((word, num))       
                break
        if not found:
            hist_tuple.append((word, 1))

    print(hist_tuple)




histogram_tuple(word_list)
