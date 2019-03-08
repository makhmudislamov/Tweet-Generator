from histograms import *
import stoc_sample
import cleaner
from cleaner import file_cleaner


def generate_sentences():
    """
    Generates sentences using random words from the source text.
    Uses stochastic sampling.
    """
    return histogram_dict(file_cleaner(cleaner.file))
    

if __name__ == '__main__':
    print(generate_sentences())
