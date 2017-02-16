# module for generating a sample word from a histogram with weights
from __future__ import division, print_function
from histogram import Dictogram
import sys
import random
import tokenize #To create lists from text files


# arguments = sys.argv[1:]  # exclude script name in first argument
# filename = arguments[0]

#Uses weighted probability to print out a random word
def random_word_weighted(filename):
    text_list = tokenize.read_in(filename)
    corpus_dict = Dictogram(text_list)
    ordered_list = (sorted(corpus_dict, key=corpus_dict.__getitem__, reverse=True))#Ordered from greatest to least.

    # print(ordered_list)
    length = corpus_dict.tokens
    random_num = random.random()
    # print("The random number is " + str(random_num))
    for weight_key in ordered_list: #Runs for each word in the histogram and subtracts the fraction of each word from the random number
        random_num -= (corpus_dict[weight_key])/length# first word was fish, second word is one, third word is red
        if random_num < 0: #Once the random number is less than 0, return that word. This will happen more often for words with bigger weighted probabilities
            return weight_key

if __name__ == '__main__':
    import sys
    arguments = sys.argv[1:]  # exclude script name in first argument
    if len(arguments) == 0:
        # test hisogram on letters in a word
        word = 'abracadabra'
        test_histogram(word)
        print()
        # test hisogram on words in a sentence
        sentence = 'one fish two fish red fish blue fish'
        word_list = sentence.split()
        test_histogram(word_list)
    elif len(arguments) == 1:
        # test hisogram on text from a file
        filename = arguments[0]
        # text_list = read_from_file(filename)
        # text_list = tokenize.read_in(filename)
        # create_histogram(filename)
        print(random_word_weighted(filename))
    else:
        # test hisogram on given arguments
        test_histogram(arguments)
