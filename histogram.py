

from __future__ import division, print_function

from hashtable import HashTable
import sys
import tokenize
import random


class Hashtogram(HashTable):

    def __init__(self, iterable=None):
        super(Hashtogram, self).__init__()
        self.triple_list = []


    def test(self):
        return self.get_random_key()

    def read_in(self, text):
        text_file = open(text, 'r') #Read text file
        word_list = [] #Create empty list to store words
        for line in text_file.readlines(): #Loop through line of words
            word_list.extend(line.split()) #Split words by white space and store as one huge list of individual words
        text_file.close()
        return word_list

    def create_input_list(self, filename):
        text_list = self.read_in(filename)
        return text_list

    # def create_input_list(self, filename):
    #     text_list = self.read_in(filename)
    #     return text_list

    #Create list of triple words from corpus
    def generate_triple(self):
        complete_list = self.create_input_list('random.txt')
        for index in range(len(complete_list)-2):
            self.triple_list.append((complete_list[index], complete_list[index + 1], complete_list[index + 2]))
        return self.triple_list

    def another_hashtogram(self):
        return Hashtogram()

    def create_markov_chain(self):
        self.new_hashtogram = self.another_hashtogram()
        for first_str, second_str, third_str in self.triple_list:
            key = (first_str, second_str)
            # print(key, third_str)
            if self.contains(key):
                self.hashtogram_for_key = self.get(key) #get the hashtogram corresponding to that key
                if self.hashtogram_for_key.contains(third_str):
                    current_key_value = self.hashtogram_for_key.get(third_str)
                    self.hashtogram_for_key.set(third_str, current_key_value + 1.0) #update frequency
                    self.set(key, self.hashtogram_for_key) #update the overall hashtogram
                else:
                    self.hashtogram_for_key.set(third_str, 1.0) #set third_str key
                    self.set(key, self.hashtogram_for_key)
            else:
                self.new_hashtogram = self.another_hashtogram()
                self.new_hashtogram.set(third_str, 1.0)
                self.set(key, self.new_hashtogram) #If the key does not exist, create the key with a value of a hashtogram with a key of the third string and a value of it's frequency
        return self

    def random_word_weighted(self, first, second):
        initial_key = first, second
        tuple_list = self.get(initial_key).items() # Get the list of tuples that is the value of the 2 word tuple key
        length = self.get(initial_key).length()
        random_num = random.random()
        for string_key, frequency in tuple_list:
            random_num -= frequency/length
            if random_num < 0: #Once the random number is less than 0, return that string. This will happen more often for words with bigger weighted probabilities
                return string_key #Return first element in random 2 word tuple
        return 0

    #create random sentence
    def generate_random_sentence(self, sentence_length):
        initial_key = self.get_random_key() #Get the initial random 2 word tuple
        sentence = ""
        first, second = initial_key[0], initial_key[1]
        for count in range(sentence_length):
            sentence += " " + first
            first, second = second, self.random_word_weighted(first, second)
        return sentence +  " "



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
        random.txt = arguments[0]
        # text_list = read_from_file(random.txt)
        # text_list = tokenize.read_in(random.txt)

        hash_t = Hashtogram()
        hash_t.generate_triple()
        hash_t.create_markov_chain()
        print(hash_t.generate_random_sentence(2))
    else:
        # test hisogram on given arguments
        test_histogram(arguments)
