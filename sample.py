# module for generating a sample word from a histogram with weights
from __future__ import division, print_function
from histogram import Dictogram  # , Hashtogram
import sys
import random
import tokenize #To create lists from text files


# arguments = sys.argv[1:]  # exclude script name in first argument
# filename = arguments[0]
def create_input_list(filename):
    text_list = tokenize.read_in(filename)
    return text_list

def create_input_dict(text_list):
    corpus_dict = Dictogram(text_list)
    return corpus_dict


#Uses weighted probability to print out a random word
def random_word_weighted(input_dict):
    ordered_list = (sorted(input_dict, key=input_dict.__getitem__, reverse=True))#Ordered from greatest to least.

    # print(ordered_list)
    length = input_dict.tokens
    random_num = random.random()
    # print("The random number is " + str(random_num))
    for weight_key in ordered_list: #Runs for each word in the histogram and subtracts the fraction of each word from the random number
        random_num -= (input_dict[weight_key])/length# first word was fish, second word is one, third word is red
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
        input_list = create_input_list(filename)
        input_dict = create_input_dict(input_list)
        print(random_word_weighted(input_dict))
    else:
        # test hisogram on given arguments
        test_histogram(arguments)
