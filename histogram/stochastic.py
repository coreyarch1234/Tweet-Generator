
import random
import sys
import histogram

# filename = raw_input("Enter name of file without the txt extension: ") + '.txt'

#This method will take in a txt file and print out a random word.
def random_word(words):
    text_list = histogram.read_in(words) #read_in creates a list of words from the text
    word_hist = histogram.histogram(text_list) #histogram creates a histogram of the words
    random_num = random.randint(0, len(text_list) - 1)
    return text_list[random_num]

def random_word_weighted(words):
    text_list = histogram.read_in(words) #read_in creates a list of words from the text
    word_hist = histogram.histogram(text_list) #histogram creates a histogram of the words
    # Order hist descending, sum the weights, subtract weight from random number loop through weights.
    # If random number is less than the weight, then return the word associated with it.
    print(sorted(word_hist, key=word_hist.__getitem__))
    sum_weights = 0.0
    length = len(word_hist)

    # for key in reverse_hist: # Gets the sum of the weights
    #     sum_weights += word_hist[key] / length
    #
    # return sum_weights

    random_num = random.random() * sum_weights

    # for weight_key in reverse_hist:
    #     random_num -= word_hist[weight_key] #takes random number (0 to 1) and subtracts the weight until the rand num is less than 0
    #     if random_num < 0: #The chances are higher of weight_key being a larger weight since it is being subtracted from random number
    #         return weight_key


if __name__ == '__main__':
    print(random_word_weighted('stochastic_random.txt'))
