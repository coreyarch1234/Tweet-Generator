
import random
import sys
import histogram


#This method will take in a txt file and print out a random word.
def random_word(words):
    text_list = histogram.read_in(words) #read_in creates a list of words from the text
    word_hist = histogram.histogram(text_list) #histogram creates a histogram of the words
    random_num = random.randint(0, len(text_list) - 1)
    return text_list[random_num]

    # print(word_hist)

if __name__ == '__main__':
    print(random_word('stochastic_random.txt'))
