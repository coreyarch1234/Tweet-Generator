from __future__ import division, print_function
import sys
import tokenize #To create lists from text files


class Dictogram(dict): #name of the class name dict

    def __init__(self, iterable=None):
        """Initialize this histogram as a new dict; update with given items"""
        super(Dictogram, self).__init__()
        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram
        if iterable:
            self.update(iterable)

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        for item in iterable:
            # TODO: increment item count
            # pass
            if item in self:
                self[item] += 1
            else:
                self[item] = 1
                self.types += 1
            self.tokens += 1

    def count(self, item):
        """Return the count of the given item in this histogram, or 0"""
        # TODO: retrieve item count
        # pass
        if item in self:
            return self[item]
        else:
            return 0
    #The total count and total number of types is taken care of. Total number of types is the same as
    #unique words.
def create_histogram(file_name):
    text_list = tokenize.read_in(filename)
    # print('text list:', text_list)
    hist_dict = Dictogram(text_list)
    # equivalent to:
    # hist_dict = Dictogram()
    # hist_dict.update(text_list)
    # print('dictogram:', hist_dict)
    return hist_dict

def test_histogram(text_list):
    print('text list:', text_list)

    hist_dict = Dictogram(text_list)
    # equivalent to:
    # hist_dict = Dictogram()
    # hist_dict.update(text_list)
    print('dictogram:', hist_dict)

    # hist_list = Listogram(text_list)
    # print('listogram:', hist_list)


# class Histogram(object):
    # def __init__(self, list):
    #     self.list = list
    #     self.types = 0 # the number of distinct item types in this histogram
    #     self.tokens = 0 # the total count of all item tokens in this histogram

    # def histogram(self, list):
    #     word_dict = {}
    #     for key_word in list:
    #         if key_word in word_dict: #If that word exists in the set
    #             word_dict[key_word] += 1 #Increment the count value
    #         else:
    #             word_dict[key_word] = 1 #Initialize it with a value
    #     return word_dict
    #
    # def unique_words(self, hist):
    #     types = len(hist.keys())
    #     return types
    #
    # def total_words(self, hist):
    #     tokens = 0
    #     for key_word in hist:
    #         tokens += hist[key_word]
    #     return tokens

    # def specific_word_count(self, word):
    #     if word in self.histogram:
    #         return self.histogram[word]
    #     else:
    #         raise 0



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
        create_histogram(filename)
    else:
        # test hisogram on given arguments
        test_histogram(arguments)



    # input_text = sys.argv[1]
    # list_object = tokenize.read_in(input_text)
    # example_hist = Histogram()
    # print example_hist.histogram(list_object)

    # print(example_hist.histogram)
    # example_hist.histogram()
    # print(example_hist)
    # print("The number of types is " + str(example_hist.unique_words()))
    # print("The number of tokens " + str(example_hist.total_words()))


    # histogram = histogram(read_in("words_alg.txt"))
    # #Finding and printing the least frequent words
    # sorted_set = sorted(histogram, key=histogram.__getitem__)
    # least_set = []
    # for least in sorted_set:
    #     if histogram[least] == histogram[sorted_set[0]]:
    #         least_set.append(least)
    # print("The least frequent words are " + str(least_set))
    #
    # #Finding and printing the  most frequent words
    # most_set = []
    # for most in sorted_set:
    #     if histogram[most] == histogram[sorted_set[-1]]:
    #         most_set.append(most)
    # print("The most frequent words and the modes are " + str(most_set))
    #
    # #Printing the number of different words
    # print("The number of distinct words are " + str(unique_words(histogram)))
    #
    # #Printing the mean
    # print("The mean of all of the words is " + str(mean(histogram)))
    #
    # #Printing the median of the words
    # print("The median of all of the words is " + str(median(histogram)))


# def read_in(text):
#     # Reading text and making the word list
#     alg = open(text, 'r')
#     alg_text = alg.readlines()
#     # word = str(raw_input()) This is if you want to find the number of times a specific word appears
#     alg_word_list = []
#     for line in alg_text:
#         alg_word_list.extend(line.split())
#     return alg_word_list

# def histogram(word_list):
#     new_word_dict = {}
#     for key_word in word_list:
#         if key_word in new_word_dict: #If that word exists in the set
#             new_word_dict[key_word] += 1 #Increment the count value
#         else:
#             new_word_dict[key_word] = 1 #Initialize it with a value
#     return new_word_dict
#
# def unique_words(histogram_input):
#     return len(histogram_input.keys())
#
# def specific_word_count(word, histogram_input):
#     if word in histogram_input:
#         return histogram_input[word]
#     else:
#         raise 0
#
# #Average of the histogram. The mean is the sum of the number of all of the occurances divided by the number of unique words
# def mean(histogram_input):
#     sum = 0.0
#     unique_count = unique_words(histogram_input)
#     for key,value in histogram_input.iteritems():
#         sum += value
#     return (sum/unique_count)
#
# #Find the median. First, sum all of the occurances, and then divide by 2, and then find the words that correspond with that frequency
# def median(histogram_input):
#     sum = mean(histogram_input) * unique_words(histogram_input)
#     median_value = sum / 2.0
#     count = 0 #keep track of the word values until it reaches the median
#     print("The median value is " + str(median_value))
#     median_array = []
#     for key,value in histogram_input.iteritems():
#         count += value
#         if count == value :
#             # print(count)
#             median_array.append(key)
#     return(median_array)
#
