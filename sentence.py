# module for generating a sentence from a histogram. Use 1st order Markov Model
# Step 1 - Create function that takes in a key and generates a list according to which words come directly after
# Step 2 - Create function that loops through all keys in corpus dictionary and for each key, insert key in first function
# to create a list. Once you have that list, input that list into Dictogram class to create dictionary and assign that dictionary
# to the value of that key. Output the dictionary of key dictionary pairs
# Step 3 - Now you have a dictionary of key dictionary pairs. To generate random sentence, input original corpus dictionary
# into random weighted to get random weighted key. Then insert that key into fucntion 2 input to get dictionary value. With that
# dictionary value, insert it back into random weighted to get a new random weighted key word. Then you will have 2 words by Markov
# model. Keep doing this for an arbitrary amount of time.

# module for generating a sample word from a histogram with weights
from __future__ import division, print_function
from histogram import Dictogram
import sys
import random
import tokenize #To create lists from text files
import sample

# Step 1
def generate_chain_list(key_word, filename):
    general_list = sample.create_input_list(filename)
    length_general = len(general_list)
    chain_list = []
    for index in range(length_general - 1):
        if general_list[index] == key_word: #better would be if you add start constant
            chain_list.append(general_list[index + 1])
    # print(chain_list)
    return chain_list #List of words that come after key word


# Step 2
def markov_model(filename):
    general_list = sample.create_input_list(filename)
    general_dict = sample.create_input_dict(general_list)
    markov_model_hash = {}
    for key in general_dict:
        key_list = generate_chain_list(key, filename)
        markov_model_hash[key] = sample.create_input_dict(key_list)
    return markov_model_hash

# Step 3
def generate_sentence(filename, sentence_length):
    general_list = sample.create_input_list(filename)
    general_dict = sample.create_input_dict(general_list)
    sentence_words = []
    markov_model_hash = markov_model(filename)
    key_word_for_sentence = sample.random_word_weighted(general_dict)
    sentence_words.append(key_word_for_sentence)
    # print(sentence_length)
    for count in range(sentence_length - 1):
        # print(sentence_words[-1])
        markov_dict = markov_model_hash[sentence_words[-1]]
        print(markov_dict)
        if markov_dict == {}:
            return (" ".join(sentence_words) + " END")
        random_word = sample.random_word_weighted(markov_dict)
        print(random_word)
        if random_word is not None:
            sentence_words.append(random_word)
    sentence = " ".join(sentence_words)
    return sentence


if __name__ == '__main__':
    import sys
    arguments = sys.argv[1:]  # exclude script name in first argument
    if len(arguments) == 0:
        print("hello")
    elif len(arguments) == 1:
        # test hisogram on text from a file
        filename = arguments[0]
        # text_list = read_from_file(filename)
        # text_list = tokenize.read_in(filename)
        # create_histogram(filename)
        # print(generate_chain_list("pagoda!", filename))
        # print(markov_model(filename))
        print(generate_sentence(filename, 120))

    else:
        print("hello world")
