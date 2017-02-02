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
    temp_word = ""
    length = len(a)
    for i in range(len(a)):
            rand_num = random.randint(0, length - 1)
            random_word = a[rand_num]
            a.remove(random_word)
            b.append(random_word)
            length -= 1
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
