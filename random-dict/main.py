#The goal is to take the words text file and create a program that takes in an integer representing
#a number of words, n,  takes a random set and outputs that set in a sentence (grammar/sentence structure does not matter)

#Handles reading text file
words = open('words.txt', 'r')
word_set = words.readlines()

word_set_list = []
for line in word_set:
    word_set_list.append(line.strip())

# for i in word_set:
#     thisline = i.split(" ")
# words.close()

#Handles reading input from user
number_of_words = map(int, raw_input())

import random
import sys

def make_list():
    for word in thisline:
        word_set_list.append(word)
    return word_set_list

def random_list(a):
    b = []
    for i in range(len(a)):
        rand_word = random.choice(a)
        a.remove(rand_word)
        b.append(rand_word)
    return b


def random_sequence():
    array = []
    random = make_list()
    print("The word is " + str(random))
    for rand in random_list(random):
        array.append(rand)
    print(array)


if __name__ == '__main__':
    random_sequence()
