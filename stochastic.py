import random
import sys
import histogram

#Prints out a random word from a histogram with no weights
def random_word():
    random_num = random.randint(0, len(text_list) - 1)
    return text_list[random_num]

#Uses weighted probability to print out a random word
def random_word_weighted():
    ordered_hist = list(reversed(sorted(word_hist, key=word_hist.__getitem__)))#Ordered from greatest to least.
    length = len(text_list) + 0.0
    random_num = random.random()
    for weight_key in ordered_hist: #Runs for each word in the histogram and subtracts the fraction of each word from the random number
        random_num -= (word_hist[weight_key])/length
        if random_num < 0: #Once the random number is less than 0, return that word. This will happen more often for words with bigger weighted probabilities
            return weight_key

#Using a test word, this will calculate how many times that word should ideally appear when taking that word randomly with weight, and will compare it with the observed case.
def percent_error(test_word, run_count):
    count = 0
    ideal_num = run_count * (word_hist[test_word])/(len(text_list) + 0.0)
    for num in range(1, run_count):
        if random_word_weighted() == test_word:
            count += 1
    print("My percent error after running " + str(run_count) + " times is " + str(100 * (count - ideal_num)/ideal_num) + "%")

if __name__ == '__main__':
    #Takes in any text file and creates a histogram named word_hist.
    filename = raw_input("Enter name of file without the txt extension: ") + '.txt'
    text_list = histogram.read_in(filename)
    word_hist = histogram.histogram(text_list)
    #Prints out the random word using weighted probability
    print random_word_weighted()
    #Uses the printed word to calculate the percent error
    percent_error("fish", 100000)
