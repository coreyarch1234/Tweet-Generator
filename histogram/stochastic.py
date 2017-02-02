
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
    ordered_hist = list(reversed(sorted(word_hist, key=word_hist.__getitem__)))
    length = len(text_list) + 0.0 #length of source text

    print(ordered_hist)

    fish_count = 0
    for num in range(1,10000):
        random_num = random.random()
        for weight_key in ordered_hist:
            random_num -= (word_hist[weight_key])/length #takes random number (0 to 1) and subtracts the weight until the rand num is less than 0

            if random_num < 0: #The chances are higher of weight_key being a larger weight since it is being subtracted from random number
                return weight_key
    #             if weight_key == "fish":
    #                 fish_count += 1
    # print("If my algorithm were perfect, the number of fish would be 5000, but my actual value is " + str(fish_count) + " the error is " + str(100 * (fish_count - 5000.0)/5000) + "%")

if __name__ == '__main__':
    print(random_word_weighted('stochastic_random.txt'))
