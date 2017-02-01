#The goal is to take the words text file and create a program that takes in an integer representing
#a number of words, n,  takes a random set and outputs that set in a sentence (grammar/sentence structure does not matter)

#Handles reading text file
def read_in(word_text):
    words = open(word_text, 'r')
    word_list = words.readlines()
    for i in word_list:
        thisline = i.split(" ")
    return thisline

#Handles reading input from user
num_count = int(raw_input())

import random
import sys

def make_list(word_list):
    this_line = read_in(word_list)
    word_list = []
    for word in this_line:
        word_list.append(word)
    return word_list

def random_list(a):
    b = []
    for i in range(len(a)):
        rand_word = random.choice(a)
        a.remove(rand_word)
        b.append(rand_word)
    return b


def random_sequence(num_count, word_list):
    array = []
    return_array = []
    random = make_list(word_list)
    for rand in random_list(random):
        array.append(rand)
    for count in range(0, num_count):
        return_array.append(array[count])
    print(return_array)


if __name__ == '__main__':
    random_sequence(num_count, 'words.txt')
